"""Rendering for the chevron Mustache engine."""

from pathlib import Path

import chevron


def setup():
    """Initial environment setup."""
    config = {}
    config["path"] = Path("pytemplates/engines/chevron/")
    return config


def render(config, template_name, variables):
    """Render template with interpolated variables."""
    with (config["path"] / template_name).open() as template:
        rendered = chevron.render(template, variables, partials_path=str(config["path"]))
    return rendered
