# Copyright 2021 Maik Derstappen
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import pdb
from odoo import api, fields, models, _


class FleetVehicleLogbook(models.Model):

    _inherit = "fleet.vehicle.odometer"
    _order = 'value DESC'
    route = fields.Char(string="Route")
    comments = fields.Char(string="Comments")

    @api.depends("value")
    def _compute_units_driven(self):
        """ Find the record with the next lesser value and calculate the difference.
        """
        odometer = self.env['fleet.vehicle.odometer']
        for ometer in self:
            results = ometer.search([('value', '<', ometer.value)], order='value DESC')
            if not results:
                ometer.units_driven = 0.0
                continue
            ometer.units_driven = ometer.value - results[0].value

    units_driven = fields.Float(
        compute="_compute_units_driven", string="Driven"
    )
