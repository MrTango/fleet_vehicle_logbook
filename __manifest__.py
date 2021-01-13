# Copyright 2021 Maik Derstappen
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Fleet Vehicle Logbook",
    "summary": "Adds some fields to fleet.vehicle.odometer, needed for a logbook",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "category": "Human Resources/Fleet",
    "author": "Maik Derstappen - Derico, Odoo Community Association (OCA)",
    "maintainers": ["mrtango",],
    "development_status": "Stable",
    "website": "https://github.com/OCA/fleet",
    "depends": ["fleet",],
    "data": ["security/fleet_vehicle_logbook.xml", "views/fleet_vehicle_logbook.xml",],
    "demo": ["demo/fleet_vehicle_logbook.xml",],
    "installable": True,
}
