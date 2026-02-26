from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Model for an offer made on a property"

    price = fields.Float("Price")
    status = fields.Selection(
        string="Status", selection=[("accepted", "Accepted"), ("refused", "Refused")]
    )
    validity = fields.Integer("Validity Length (Days)", required=True, default=7)
    deadline_date = fields.Date("Response Deadline", required=True)
    partner_id = fields.Many2one("res.partner", string="Buyer", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
