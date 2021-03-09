# Copyright 2021 Maik Derstappen
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import pdb
from odoo import api, fields, models, _


class FleetVehicleLogbook(models.Model):

    _inherit = "fleet.vehicle.odometer"
    _order = "value DESC"
    route = fields.Char(string="Route")
    comments = fields.Char(string="Comments")

    # override driver to avoid updating the vehicle when we change the driver here
    driver_id = fields.Many2one(
        "res.partner",
        "Driver",
        related=None,
        help="Driver of the vehicle",
        copy=False,
        default=lambda self: self.env.user.partner_id,
    )

    @api.onchange('vehicle_id')
    def onchange_vehicle_id(self):
        """ set the vehicle driver as default
        """
        if self.driver_id:
            return
        if self.vehicle_id:
            self.driver_id = self.env.user.partner_id

    units_driven = fields.Float(compute="_compute_units_driven", string="Driven")

    @api.depends("value")
    def _compute_units_driven(self):
        """ Find the record with the next lesser value and calculate the difference.
        """
        for ometer in self:
            results = ometer.search([("value", "<", ometer.value)], order="value DESC")
            if not results:
                ometer.units_driven = 0.0
                continue
            ometer.units_driven = ometer.value - results[0].value
