from odoo import api, fields, models
from datetime import timedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

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
    active = fields.Boolean("Active", default=True)
    state = fields.Selection(
        string="State",
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("sold", "Sold"),
            ("cancelled", "Cancelled"),
        ],
        required=True,
        copy=False,
        default="new",
    )
    type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    seller_id = fields.Many2one(
        "res.users", default=lambda self: self.env.user, string="Seller"
    )
    tag_ids = fields.Many2many("estate.property.tag", string="Property Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offer")
    total_area = fields.Float(compute="_get_total_area")
    best_offer = fields.Float(compute="_get_best_offer")

    @api.depends("living_area", "garden_area")
    def _get_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _get_best_offer(self):
        for record in self:
            best_offer_so_far = 0
            if len(record.offer_ids) > 0:
                prices = record.offer_ids.mapped("price")
                for price in prices:
                    if best_offer_so_far < price:
                        best_offer_so_far = price
            record.best_offer = best_offer_so_far

    @api.onchange("has_garden")
    def _onchange_has_garden(self):
        if self.has_garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = None
            self.garden_orientation = None
