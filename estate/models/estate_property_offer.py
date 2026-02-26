from __future__ import annotations
from odoo import api, fields, models
from datetime import timedelta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .estate_property import EstateProperty


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Model for an offer made on a property"

    _sql_constraints = [
        (
            "check_offer_price_positive",
            "CHECK(price > 0)",
            "Offer price must be positive.",
        )
    ]

    price = fields.Float("Price")
    status = fields.Selection(
        string="Status", selection=[("accepted", "Accepted"), ("refused", "Refused")]
    )
    validity = fields.Integer("Validity Length (Days)", required=True, default=7)
    deadline_date = fields.Date(
        compute="_compute_deadline",
        inverse="_inverse_deadline",
        string="Deadline Date",
    )
    partner_id = fields.Many2one("res.partner", string="Buyer", required=True)
    property_id: EstateProperty = fields.Many2one(
        "estate.property", string="Property", required=True
    )

    @api.depends("validity")
    def _compute_deadline(self):
        for record in self:
            if record.create_date:
                record.deadline_date = record.create_date.date() + timedelta(
                    days=record.validity
                )
            else:
                record.deadline_date = fields.Date.today() + timedelta(
                    days=record.validity
                )

    @api.onchange("deadline_date")
    def _inverse_deadline(self):
        for record in self:
            if record.create_date:
                delta = record.deadline_date - record.create_date.date()
                record.validity = delta.days
            else:
                delta = record.deadline_date - fields.Date.today()
                record.validity = delta.days

    def accept_offer(self):
        for record in self:
            if record.property_id:
                record.property_id.selling_price = self.price
                record.property_id.buyer_id = self.partner_id
                record.status = "accepted"
        return True

    def reject_offer(self):
        for record in self:
            record.status = "refused"
        return True
