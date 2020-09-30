"""Rendering for wheezy templates."""

from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import DictLoader, FileLoader

INCLUDES_RE = r"@extends\(['\"]([^'\"]+)['\"]\)"


def compile_template(template_dict, template_name):
    """Compile template."""
    engine = Engine(loader=DictLoader(template_dict), extensions=[CoreExtension()])
    compiled = engine.get_template(template_name)
    return compiled


def render_compiled(compiled, variables):
    """Render from compiled template with interpolated variables."""
    return compiled.render(variables)


def render_from_file(template_file, variables):
    """Render from template string with interpolated variables."""
    searchpath = [str(template_file.resolve().parent)]
    engine = Engine(loader=FileLoader(searchpath), extensions=[CoreExtension()])
    template = engine.get_template(template_file.name)
    return template.render(variables)
