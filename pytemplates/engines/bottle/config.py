"""Rendering for bottle.py SimpleTemplate engine."""

from bottle import SimpleTemplate

INCLUDES_RE = r"%\s+(?:rebase|include)\(['\"]([^'\"]+)['\"][^\)]*\)"


def compile_template(template_dict, template_name):
    """Compile template."""
    compiled = SimpleTemplate(name=template_name, source=template_dict[template_name])
    compiled.cache = {
        name: SimpleTemplate(name=name, source=template_dict[name])
        for name in template_dict
        if name != template_name
    }
    return compiled


def render_compiled(compiled, variables):
    """Render from compiled template with interpolated variables."""
    return compiled.render(**variables)


def render_from_file(template_file, variables):
    """Render from file with interpolated variables."""
    template = SimpleTemplate(name=template_file.name, lookup=[template_file.parent])
    return template.render(**variables)
