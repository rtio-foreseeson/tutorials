from odoo import api, fields, models
from datetime import timedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Model for an offer made on a property"

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
    property_id = fields.Many2one("estate.property", string="Property", required=True)

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
