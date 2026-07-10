# Copyright 2026 Altixia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import re

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    passport_number = fields.Char()
    passport_expiration = fields.Date()

    @api.constrains("passport_number", "nationality_id")
    def _check_passport_number(self):
        """Soft validation: only enforce the format when one is defined for the
        partner's nationality. Unknown countries are left untouched."""
        fmt_model = self.env["res.partner.passport.format"]
        for partner in self:
            number = (partner.passport_number or "").strip()
            country = partner.nationality_id
            if not number or not country:
                continue
            fmt = fmt_model.search([("country_id", "=", country.id)], limit=1)
            if not fmt:
                continue
            if not re.fullmatch(fmt.pattern, number.upper()):
                raise ValidationError(
                    _(
                        "The passport number '%(number)s' does not match the "
                        "expected format for %(country)s (%(description)s).",
                        number=number,
                        country=country.name,
                        description=fmt.name or fmt.pattern,
                    )
                )
