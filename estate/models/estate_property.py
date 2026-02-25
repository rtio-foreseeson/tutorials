from odoo import fields, models
from datetime import timedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    # _order = "sequence"

    name = fields.Char("Property Name", required=True)
    description = fields.Char("Description")
    postcode = fields.Char("Postcode")
    date_available = fields.Date(
        "Available From", copy=False, default=fields.Date.today() + timedelta(days=90)
    )
    expected_price = fields.Float("Expected Price")
    best_offer = fields.Float("Best Offer", copy=False)
    selling_price = fields.Float("Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default=2)
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
