"""Rendering for Jinja2 engine."""

from jinja2 import Environment, DictLoader, FileSystemLoader

INCLUDES_RE = r"{%\s*extends\s+['\"]([^'\"]+)['\"]\s*%}"


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


def compile_template(template_dict, template_name):
    """Compile template."""
    env = Environment(loader=DictLoader(template_dict))
    template = env.get_template(template_name)
    return template


def render_compiled(compiled, variables):
    """Render from compiled template with interpolated variables."""
    return compiled.render(**variables)


def render_from_file(template_file, variables):
    """Render from template string with interpolated variables."""
    env = Environment(loader=FileSystemLoader(template_file.parent))
    template = env.get_template(template_file.name)
    return template.render(**variables)
