"""Rendering for bottle.py SimpleTemplate engine."""

from pathlib import Path

from bottle import SimpleTemplate


def setup():
    """Initial environment setup."""
    config = {}
    config["path"] = Path("pytemplates/engines/bottle/")
    return config


def render(config, template_name, variables):
    """Render template with interpolated variables."""
    template = SimpleTemplate(name=template_name, lookup=[config["path"]])
    return template.render(**variables)
