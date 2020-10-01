"""Rendering for bottle.py SimpleTemplate engine."""

from bottle import SimpleTemplate

INCLUDES_RE = r"%\s+(?:rebase|include)\(['\"]([^'\"]+)['\"][^\)]*\)"


def compile_template(template_dict, template_name):
    """Compile template."""
    templates = template_dict.copy()
    compiled = SimpleTemplate(name=template_name, source=templates.pop(template_name))
    compiled.cache = {
        name: SimpleTemplate(name=name, source=templates[name]) for name in templates
    }
    return compiled


def render_compiled(compiled, variables):
    """Render from compiled template with interpolated variables."""
    return compiled.render(**variables)


def render_from_file(template_file, variables):
    """Render from file with interpolated variables."""
    return SimpleTemplate(name=template_file.name, lookup=[template_file.parent])
