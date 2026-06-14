# Copyright 2026 Altixia (https://altixia.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestPartnerPhoneExtension(TransactionCase):
    def test_phone_extension_stored(self):
        partner = self.env["res.partner"].create(
            {"name": "Ext Test", "phone_extension": "123"}
        )
        self.assertEqual(partner.phone_extension, "123")
