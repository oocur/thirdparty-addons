{
    "name": "oocur_testfix",
    "version": "1.0.0",
    "category": "Hidden",
    "summary": "Resolves asset conflicts between third-party addons at test time",
    "description": """
Purpose:
- Resolve asset/view incompatibilities when both addons are installed.

First conflict:
- muk_web_theme + web_responsive navbar clash.

Approach:
- Remove muk_web_theme's navbar override via an ir.asset remove directive.

Notes:
- No third-party code modifications required.

Extensibility:
- Add new conflicts in data/ and update dependencies.
""",
    "author": "oocur",
    "website": "https://github.com/oocur",
    "depends": ["base", "muk_web_theme", "web_responsive"],
    "data": ["data/ir_asset_removes.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
