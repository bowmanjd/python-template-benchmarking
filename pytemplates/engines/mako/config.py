"""Rendering for Mako templates."""

from mako.lookup import TemplateLookup


def setup():
    """Initial environment setup."""
    config = {}
    config["lookup"] = TemplateLookup(directories=["/home/jbowman/devel/pytemplates/pytemplates/engines/mako/"])
    return config


def render(config, template_name, variables):
    """Render template with interpolated variables."""
    template = config["lookup"].get_template(template_name)
    return template.render(**variables)
