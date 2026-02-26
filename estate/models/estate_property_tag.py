from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "A tag describing a property e.g. Cozy, Renovated"

    name = fields.Char("Name", required=True)
