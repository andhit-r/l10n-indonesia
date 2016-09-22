# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# Copyright 2016 Prime Force Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Indonesia - Formulir Pajak",
    "version": "8.0.1.0.0",
    "category": "localization",
    "website": "https://odoo-community.org/",
    "author": "OpenSynergy Indonesia,"
              "Prime Force Indonesia,"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "data/ptkp_category_data.xml",
        "menu.xml",
        "views/tax_period_views.xml",
        "views/ptkp_views.xml",
    ],
    "demo": [
        "demo/tax_period_demo.xml",
        ],
}
