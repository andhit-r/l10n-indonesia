# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# Copyright 2016 Prime Force Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.tests.common import TransactionCase
from datetime import datetime


class TestTaxform1721(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestTaxform1721, self).setUp(*args, **kwargs)
        self.obj_taxform = self.env["l10n_id.taxform_1721_a1"]
        self.company = self.env.ref("base.main_company")
        self.employee = self.env.ref("hr.employee")
        self.tax_period = self.env.ref("l10n_id_taxform.period_7")


    def _create_taxform(self,
                        date=False,
                        tax_period_id=False,
                        bruto_1=0.0,
                        bruto_2=0.0,
                        bruto_3=0.0,
                        bruto_4=0.0,
                        bruto_5=0.0,
                        bruto_6=0.0,
                        bruto_7=0.0,
                        deduction_1=0.0,
                        deduction_2=0.0,
                        ):
        if not tax_period_id:
            tax_period_id = self.tax_period.id

        if not date:
            date = datetime.now().strftime("%Y-%m-%d")

        data = {
            "company_id": self.company.id,
            "employee_id": self.employee.id,
            "date": date,
            "tax_period_id": self.tax_period.id,
            "bruto_1": bruto_1,
            "bruto_2": bruto_2,
            "bruto_3": bruto_3,
            "bruto_4": bruto_4,
            "bruto_5": bruto_5,
            "bruto_6": bruto_6,
            "bruto_7": bruto_7,
            "deduction_1": deduction_1,
            "deduction_2": deduction_2,
            }
        taxform = self.obj_taxform.create(data)

        return taxform

    def _confirm_taxform(self, taxform):
        taxform.action_confirm()
        self.assertEqual(
            taxform.state,
            "confirm")
        #TODO: Another Check

    def _valid_taxform(self, taxform):
        taxform.action_valid()
        self.assertEqual(
            taxform.state,
            "valid")
        #TODO: Another Check


    def _cancel_taxform(self, taxform):
        taxform.action_cancel()
        self.assertEqual(
            taxform.state,
            "cancel")
        #TODO: Another Check

    def test_1(self):
        # User create a taxform
        taxform = self._create_taxform()
        # User then confirm it
        self._confirm_taxform(taxform)
        # User then validate it
        self._valid_taxform(taxform)

    def test_2(self):
        # User create a taxform
        taxform = self._create_taxform()
        # User then cancel it
        self._cancel_taxform(taxform)

    def test_3(self):
        # User create a taxform
        taxform = self._create_taxform()
        # User then confirm it
        self._confirm_taxform(taxform)
        # User then cancel it
        self._cancel_taxform(taxform)

    def test_4(self):
        # User create a taxform
        taxform = self._create_taxform()
        # User then confirm it
        self._confirm_taxform(taxform)
        # User then validate it
        self._valid_taxform(taxform)
        # User then cancel it
        self._cancel_taxform(taxform)
