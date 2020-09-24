"""Rendering for Liquidpy engine."""

from pathlib import Path

from liquid import Liquid


def setup():
    """Initial environment setup."""
    config = {"path": Path("pytemplates/engines/liquidpy/")}
    return config


def render(config, template_name, variables):
    """Render template with interpolated variables."""
    template = Liquid(str(config["path"] / template_name), liquid_from_file=True)
    return template.render(**variables)
