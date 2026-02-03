# oocur_testfix

## Purpose
Resolve asset/view incompatibilities between third-party addons when both are installed (e.g., devcontainer, Lane-B tests).

## First Conflict
- `muk_web_theme` + `web_responsive` both extend `web.NavBar.AppsMenu` with `<xpath expr="//Dropdown" position="replace">`.
- The second replacement fails with "Element cannot be located in element tree".
- Solution: remove `muk_web_theme`'s navbar override so only `web_responsive`'s is applied.

## How It Works
- Module depends on both conflicting addons.
- Only installable when both are present.
- Uses an `ir.asset` remove directive to exclude `muk_web_theme/static/src/webclient/navbar/navbar.xml` from `web.assets_backend`.
- No changes to third-party code required.

## Adding Future Conflicts
- Create a new data file in `data/` (e.g., `ir_asset_removes_other.xml`).
- Add a `<record model="ir.asset">` with an appropriate remove directive.
- Add conflicting modules to `depends` in `__manifest__.py`.
- Add the new data file to the `data` list in `__manifest__.py`.
- Document the new conflict in this README.

## Verification
After implementation, run `bash scripts/testing/devcontainer/test-lane-b-devcon.sh` and verify the web client loads without an OwlError at `http://127.0.0.1:8069`.
