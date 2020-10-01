"""Rendering for Mako templates."""

from mako.lookup import TemplateLookup

INCLUDES_RE = r"<%inherit\s+file=['\"]([^'\"]+)['\"][^>]*>"


def compile_template(template_dict, template_name):
    """Compile template."""
    lookup = TemplateLookup(filesystem_checks=False)
    for name, template in template_dict.items():
        lookup.put_string(name, template)
    compiled = lookup.get_template(template_name)
    return compiled


def render_compiled(compiled, variables):
    """Render from compiled template with interpolated variables."""
    return compiled.render(**variables)


def render_from_file(template_file, variables):
    """Render from file with interpolated variables."""
    lookup = TemplateLookup(directories=[template_file.parent])
    template = lookup.get_template(template_file.name)
    return template.render(**variables)
