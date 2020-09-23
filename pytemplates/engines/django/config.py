"""Rendering for Django templates."""

import django.template


def setup():
    """Configure environment for template loading, etc."""
    config = {}
    config["engine"] = django.template.Engine(dirs=["pytemplates/engines/django"])
    return config


def render(config, template_name, variables):
    """Render template with interpolated variables."""
    template = config["engine"].get_template(template_name)
    context = django.template.Context(variables)
    return template.render(context)
