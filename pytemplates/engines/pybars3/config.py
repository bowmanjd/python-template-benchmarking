"""Rendering for the chevron Mustache engine."""

from pathlib import Path

from pybars import Compiler

INCLUDES_RE = r"{{>\s+(\S+)\s*}}"
INCLUDES_EXT = ".hbs"


def setup():
    """Initial environment setup."""
    config = {}
    config["compiler"] = Compiler()
    config["path"] = Path("pytemplates/engines/pybars3/")
    config["partials"] = {
        f.stem: config["compiler"].compile(f.read_text())
        for f in config["path"].glob("*.hbs")
    }
    return config


def render(config, template_name, variables):
    """Render template with interpolated variables."""
    source = (config["path"] / template_name).read_text()
    template = config["compiler"].compile(source, path=str(config["path"]))
    rendered = template(variables, partials=config["partials"])
    return rendered


def compile_template(template_dict, template_name):
    """Compile template."""
    compiler = Compiler()
    partials = {
        name: compiler.compile(template)
        for name, template in template_dict.items()
        if name != template_name
    }
    compiled = compiler.compile(template_dict[template_name])
    return compiled, partials


def render_compiled(compiled, variables):
    """Render from compiled template with interpolated variables."""
    template, partials = compiled
    return template(variables, partials=partials)


def render_from_file(template_file, variables):
    """Render from template string with interpolated variables."""
    compiler = Compiler()
    partials = {
        f.stem: compiler.compile(f.read_text())
        for f in template_file.parent.glob("*.hbs")
    }
    source = template_file.read_text()
    template = compiler.compile(source, path=str(template_file.parent))
    return template(variables, partials=partials)
