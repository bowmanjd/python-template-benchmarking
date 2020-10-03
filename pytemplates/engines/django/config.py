"""Rendering for Django templates."""

import django.template

INCLUDES_RE = r"{%\s*extends\s+['\"]([^'\"]+)['\"]\s*%}"


def compile_template(template_dict, template_name):
    """Compile template."""
    engine = django.template.Engine(
        loaders=[("django.template.loaders.locmem.Loader", template_dict)]
    )
    template = engine.get_template(template_name)
    return template


def render_compiled(compiled, variables):
    """Render from compiled template with interpolated variables."""
    context = django.template.Context(variables)
    return compiled.render(context)


def render_from_file(template_file, variables):
    """Render from template string with interpolated variables."""
    engine = django.template.Engine(dirs=[template_file.parent])
    template = engine.get_template(template_file.name)
    context = django.template.Context(variables)
    return template.render(context)
