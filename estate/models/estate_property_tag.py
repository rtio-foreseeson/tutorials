from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "A tag describing a property e.g. Cozy, Renovated"
    _sql_constraints = [
        (
            "check_property_tag_name_unique",
            "UNIQUE(name)",
            "Property tag name must be unique.",
        )
    ]

    name = fields.Char("Name", required=True)
