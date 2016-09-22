# -*- coding: utf-8 -*-
# Copyright 2016 Prime Force Indo
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api

PERIOD_SELECTION = map(lambda x: [x, str(x)], range(1, 13))


class Taxform1721A1(models.Model):
    _name = "l10n_id.taxform_1721_a1"
    _description = "Taxform 1721 A1"

    @api.model
    def _default_employee_id(self):
        #TODO
        return False

    @api.model
    def _default_company_id(self):
        #TODO
        return False

    @api.model
    def _default_date(self):
        #TODO
        return False

    @api.multi
    @api.depends(
        "date", "employee_id",
        "bruto_1", "bruto_2", "bruto_2", "bruto_3",
        "bruto_4", "bruto_5", "bruto_6", "bruto_7",
        "deduction_1", "deduction_2",
        )
    def _compute_all(self):
        #TODO
        for taxform in self:
            taxform.ptkp_line_id = False
            taxform.ptkp_category_id = False
            taxform.bruto_8 = taxform.deduction_3 = taxform.computation_1 = \
                    taxform.computation_2 = taxform.computation_3 = \
                    taxform.computation_4 = taxform.computation_5 = \
                    taxform.computation_6 = taxform.computation_7 = \
                    taxform.computation_8 = 0.0



    name = fields.Char(
        string="# Formulir",
        required=True,
        readonly=True,
        default="/",
        )
    date = fields.Date(
        string="Tanggal Potongan",
        required=True,
        )
    employee_id = fields.Many2one(
        string="Karyawan",
        comodel_name="hr.employee",
        required=True,
        )
    company_id = fields.Many2one(
        string="Pemotong Pajak",
        comodel_name="res.company",
        required=True,
        )
    tax_period_id = fields.Many2one(
        string="Masa Pajak",
        comodel_name="l10n_id.tax_period",
        required=True,
        )
    tax_year_id = fields.Many2one(
        string="Tahun Pajak",
        comodel_name="l10n_id.tax_year",
        related="tax_period_id.year_id",
        store=True,
        readonly=True,
        )
    ptkp_line_id = fields.Many2one(
        string="Tarif PTKP",
        compute="_compute_all",
        comodel_name="l10n_id.ptkp_line",
        store=True,
        )
    ptkp_category_id = fields.Many2one(
        string="Kategori PTKP",
        compute="_compute_all",
        comodel_name="l10n_id.ptkp_category",
        store=True,
        )
    bruto_1 = fields.Float(
        string="Bruto Item 1",
        )
    bruto_2 = fields.Float(
        string="Bruto Item 2",
        )
    bruto_3 = fields.Float(
        string="Bruto Item 3",
        )
    bruto_4 = fields.Float(
        string="Bruto Item 4",
        )
    bruto_5 = fields.Float(
        string="Bruto Item 5",
        )
    bruto_6 = fields.Float(
        string="Bruto Item 6",
        )
    bruto_7 = fields.Float(
        string="Bruto Item 7",
        )
    bruto_8 = fields.Float(
        string="Bruto Item 8",
        compute="_compute_all",
        store=True,
        )
    deduction_1 = fields.Float(
        string="Deduction Item 1",
        )
    deduction_2 = fields.Float(
        string="Deduction Item 2",
        )
    deduction_3 = fields.Float(
        string="Deduction Item 3",
        compute="_compute_all",
        store=True,
        )
    computation_1 = fields.Float(
        string="Computation Item 1",
        compute="_compute_all",
        store=True,
        )
    computation_2 = fields.Float(
        string="Computation Item 2",
        compute="_compute_all",
        store=True,
        )
    computation_3 = fields.Float(
        string="Computation Item 3",
        compute="_compute_all",
        store=True,
        )
    computation_4 = fields.Float(
        string="Computation Item 4",
        compute="_compute_all",
        store=True,
        )
    computation_5 = fields.Float(
        string="Computation Item 5",
        compute="_compute_all",
        store=True,
        )
    computation_6 = fields.Float(
        string="Computation Item 6",
        compute="_compute_all",
        store=True,
        )
    computation_7 = fields.Float(
        string="Computation Item 7",
        compute="_compute_all",
        store=True,
        )
    computation_8 = fields.Float(
        string="Computation Item 8",
        compute="_compute_all",
        store=True,
        )
    computation_9 = fields.Float(
        string="Computation Item 9",
        compute="_compute_all",
        store=True,
        )
    confirm_date = fields.Datetime(
        string="Confirm Time",
        readonly=True,
        )
    confirm_uid = fields.Many2one(
        string="Confirmed By",
        comodel_name="res.users",
        readonly=True,
        )
    valid_date = fields.Datetime(
        string="Valid Time",
        readonly=True,
        )
    valid_uid = fields.Many2one(
        string="Validated By",
        comodel_name="res.users",
        readonly=True,
        )
    cancel_date = fields.Datetime(
        string="Valid Time",
        readonly=True,
        )
    cancel_uid = fields.Many2one(
        string="Validated By",
        comodel_name="res.users",
        readonly=True,
        )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting For Approval"),
            ("valid", "Valid"),
            ("cancel", "Cancel"),
            ],
        readonly=True,
        required=True,
        default="draft",
        )

    @api.multi
    def action_draft(self):
        for taxform in self:
            data = self._prepare_draft_data()
            self.write(data)

    @api.multi
    def action_confirm(self):
        for taxform in self:
            data = self._prepare_confirm_data()
            self.write(data)

    @api.multi
    def action_valid(self):
        for taxform in self:
            data = self._prepare_valid_data()
            self.write(data)

    @api.multi
    def action_cancel(self):
        for taxform in self:
            data = self._prepare_cancel_data()
            self.write(data)

    @api.multi
    def _prepare_draft_data(self):
        self.ensure_one()
        #TODO
        data = {}
        return data

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        #TODO
        data = {}
        return data

    @api.multi
    def _prepare_valid_data(self):
        self.ensure_one()
        #TODO
        data = {
            "name": self._generate_sequence(),
            }
        return data

    @api.multi
    def _prepare_cancel_data(self):
        self.ensure_one()
        #TODO
        data = {}
        return data

    @api.multi
    def _generate_sequence(self):
        self.ensure_one()
        #TODO
        name = ""
        return name
