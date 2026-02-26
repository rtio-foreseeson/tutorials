from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "A type for a property (e.g. Apartment, House)"
    _sql_constraints = [
        (
            "check_property_type_name_unique",
            "UNIQUE(name)",
            "Property type name must be unique.",
        )
    ]

    name = fields.Char("Name", required=True)
