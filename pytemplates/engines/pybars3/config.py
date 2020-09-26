"""Rendering for the chevron Mustache engine."""

from pathlib import Path

from pybars import Compiler


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
