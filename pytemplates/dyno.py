"""Render templates using designated engines."""

import importlib
import re
from functools import lru_cache
from pathlib import Path

VARIABLES = {
    "author": "Jonathan Bowman",
    "category": "Templates",
    "date": "2055-03-05",
    "links": [
        {"url": "https://www.wikipedia.org/", "text": "Wikipedia"},
        {"url": "https://www.python.org/", "text": "Python"},
        {
            "url": "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "text": "Python Wikipedia",
        },
        {
            "url": "https://simple.wikipedia.org/wiki/Python_(programming_language)",
            "text": "Python Simple Wikipedia",
        },
        {
            "url": "https://en.wikipedia.org/wiki/History_of_Python",
            "text": "History of Python",
        },
        {"url": "https://en.wikipedia.org/wiki/Pythonidae", "text": "The Snake"},
        {"url": "https://en.wikipedia.org/wiki/Monty_Python", "text": "The Troupe"},
    ],
    "tags": [
        "HTML",
        "Text",
        "Web development",
        "Interpolation",
        "Templating",
        "Python",
        "Automation",
        "Dynamic",
        "Laziness",
        "Developers",
        "Flexibility",
    ],
    "title": "Python Templating Engines",
    "var1": "Nobody",
    "var2": "expects",
    "var3": "the",
    "var4": "Spanish",
    "var5": "Inquisition!",
    "var6": "A",
    "var7": "newt?",
    "var8": "Well,",
    "var9": "I",
    "var10": "got",
    "var11": "better.",
}

VARIABLES["tagstring"] = ", ".join(VARIABLES["tags"])


def compile_and_render(engine, template_name):
    """Compile and render designated template with designated engine."""
    compiled_template = precompile(engine, template_name)
    return engine.config.render_compiled(compiled_template, VARIABLES)


@lru_cache
def get_template_dict(engine, template_name):
    """Load main and associated templates."""
    template_string, template_path = read_template(engine, template_name)
    template_dict = {template_name: template_string}
    includes_re = re.compile(engine.config.INCLUDES_RE)
    try:
        includes_ext = engine.config.INCLUDES_EXT
    except AttributeError:
        includes_ext = ""
    populate_dict(
        template_string, template_path, includes_re, template_dict, includes_ext
    )
    return template_dict


def get_template_file(engine, template_name):
    """Get template path."""
    template_path = Path(engine.__name__.replace(".", "/"))
    template_file = template_path / template_name
    return template_file


def import_engine(module_name):
    """Import designated engine by name."""
    engine = importlib.import_module(f"pytemplates.engines.{module_name}")
    engine.config = importlib.import_module(".config", engine.__name__)
    return engine


def populate_dict(template, template_path, includes_re, template_dict, includes_ext=""):
    """Recursively populate template dict."""
    template_names = includes_re.findall(template)
    for template_name in template_names:
        if template_name not in template_dict:
            template_dict[template_name] = (
                template_path / f"{template_name}{includes_ext}"
            ).read_text()
            populate_dict(
                template_dict[template_name], template_path, includes_re, template_dict
            )
    return template_dict


def precompile(engine, template_name):
    """Compile designated template with designated engine."""
    # template_string, template_path = read_template(engine, template_name)

    # return engine.config.compile_template(template_string, template_path, template_dict)
    template_dict = get_template_dict(engine, template_name)
    return engine.config.compile_template(template_dict, template_name)


def read_template(engine, template_name):
    """Read template string from file and get path."""
    template_file = get_template_file(engine, template_name)
    template_string = template_file.read_text()
    return template_string, template_file.parent


def render_compiled(engine, compiled_template):
    """Render designated compiled template with designated engine."""
    return engine.config.render_compiled(compiled_template, VARIABLES)


def render_from_file(engine, template_name):
    """Render designated template with designated engine, loading from filesystem."""
    template_file = get_template_file(engine, template_name)
    return engine.config.render_from_file(template_file, VARIABLES)
