# -*- coding: utf-8 -*-
# Copyright 2016 Prime Force Indonesia
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class TaxYear(models.Model):
    _name = "l10n_id.tax_year"
    _description = "Tax Year"

    name = fields.Char(
        string="Tax Year",
        required=True,
        )
    code = fields.Char(
        string="Code",
        required=True,
        )
    date_start = fields.Date(
        string="Date Start",
        required=True,
        )
    date_end = fields.Date(
        string="Date End",
        required=True,
        )
    period_ids = fields.One2many(
        string="Periods",
        comodel_name="l10n_id.tax_period",
        inverse_name="year_id",
        )

class TaxPeriod(models.Model):
    _name = "l10n_id.tax_period"
    _description = "Tax Period"


    name = fields.Char(
        string="Tax Period",
        required=True,
        )
    code = fields.Char(
        string="Code",
        required=True,
        )
    date_start = fields.Date(
        string="Date Start",
        required=True,
        )
    date_end = fields.Date(
        string="Date End",
        required=True,
        )
    year_id = fields.Many2one(
        string="Tax Year",
        comodel_name="l10n_id.tax_year",
        ondelete="cascade",
        )
