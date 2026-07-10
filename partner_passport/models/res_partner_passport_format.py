# Copyright 2026 Altixia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import re

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartnerPassportFormat(models.Model):
    _name = "res.partner.passport.format"
    _description = "Passport Number Format"
    _order = "country_id"

    country_id = fields.Many2one(
        "res.country", string="Country", required=True, ondelete="cascade"
    )
    pattern = fields.Char(
        required=True,
        help="Regular expression the passport number must fully match. "
        "The number is stripped and upper-cased before checking.",
    )
    name = fields.Char(
        string="Description",
        help="Human-readable format, e.g. '2 letters + 6 digits'.",
    )

    _sql_constraints = [
        (
            "country_uniq",
            "unique(country_id)",
            "A passport format already exists for this country.",
        ),
    ]

    @api.constrains("pattern")
    def _check_pattern(self):
        for rec in self:
            try:
                re.compile(rec.pattern)
            except re.error as err:
                raise ValidationError(
                    _(
                        "Invalid regular expression '%(pattern)s': %(error)s",
                        pattern=rec.pattern,
                        error=err,
                    )
                ) from err
