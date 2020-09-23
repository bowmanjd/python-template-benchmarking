"""Rendering for Jinja2 engine."""

from jinja2 import Environment, FileSystemLoader


def setup():
    """Initial environment setup."""
    config = {}
    config["environment"] = Environment(
        loader=FileSystemLoader("pytemplates/engines/jinja2")
    )
    return config


def render(config, template_name, variables):
    """Render template with interpolated variables."""
    template = config["environment"].get_template(template_name)
    return template.render(**variables)
