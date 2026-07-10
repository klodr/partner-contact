This module adds passport information to contacts, in the *Personal Information*
page, right after the nationality:

- **Passport Number**
- **Passport Expiration**

It also provides a configurable, per-country table of passport number formats
(regular expressions), pre-loaded for the main countries. When a contact has a
nationality for which a format is defined, the passport number is validated
against that format to catch typing mistakes. Countries without a defined format
are left untouched (soft validation).
