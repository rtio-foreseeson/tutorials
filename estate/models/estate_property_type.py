from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "A type for a property (e.g. Apartment, House)"

    name = fields.Char("Name", required=True)
