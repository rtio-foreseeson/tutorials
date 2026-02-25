from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property.type"

    name = fields.Char("Name", required=True)
