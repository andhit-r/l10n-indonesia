# -*- coding: utf-8 -*-
# Copyright 2016 Prime Force Indo
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Indonesia - Formulir Pajak 1721-A1",
    "version": "8.0.1.0.0",
    "category": "Human ",
    "website": "https://odoo-community.org/",
    "author": "Prime Force Indonesia,"
              "OpenSynergy Indonesia,"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "hr_payroll",
        "l10n_id_taxform",
    ],
    "data": [
        "views/taxform_1721_a1_views.xml",
    ],
}
