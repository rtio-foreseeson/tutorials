from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    # _order = "sequence"

    name = fields.Char("Property Name", required=True)
    description = fields.Char("Description")
    postcode = fields.Char("Postcode")
    date_available = fields.Date("Available From")
    expected_price = fields.Float("Expected Price", required=True)
    best_offer = fields.Float("Best Offer")
    selling_proce = fields.Float("Selling Price")
    bedrooms = fields.Integer("Bedrooms")
    living_area = fields.Integer("Living Area (sqft)")
    facades = fields.Integer("Facades")
    has_garage = fields.Boolean("Garage")
    has_garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[
            ("north", "North"),
            ("east", "East"),
            ("south", "South"),
            ("west", "West"),
        ],
    )
