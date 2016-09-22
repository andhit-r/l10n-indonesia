# -*- coding: utf-8 -*-
# Copyright 2016 Prime Force Indonesia
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PtkpCategory(models.Model):
    _name = "l10n_id.ptkp_category"
    _description = "Kategori PTKP"

    name = fields.Char(
        string="Category",
        required=True,
        )
    note = fields.Text(
        string="Additional Note",
        )

class Ptkp(models.Model):
    _name = "l10n_id.ptkp"
    _description = "Tarif PTKP"

    name = fields.Char(
        string="Dasar Hukum",
        required=True,
        )
    date_start = fields.Date(
        string="Tanggal Mulai Berlaku",
        required=True,
        )
    date_end = fields.Date(
        string="Tanggal Selesai Berlaku",
        )
    line_ids = fields.One2many(
        string="Detail Tarif",
        comodel_name="l10n_id.ptkp_line",
        inverse_name="ptkp_id",
        )

class PtkpLine(models.Model):
    _name = "l10n_id.ptkp_line"
    _description = "PTKP Line"

    ptkp_id = fields.Many2one(
        string="PTKP",
        comodel_name="l10n_id.ptkp",
        ondelete="cascade",
        )
    ptkp_category_id = fields.Many2one(
        string="PTKP Category",
        comodel_name="l10n_id.ptkp_category",
        required=True,
        )
    ptkp_rate = fields.Float(
        string="Tarif PTKP",
        required=True,
        )
