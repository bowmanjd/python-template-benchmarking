"""Render templates using designated engines."""

import importlib

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


def import_engine(module_name):
    """Import designated engine by name."""
    engine = importlib.import_module(f"pytemplates.engines.{module_name}")
    engine.config = importlib.import_module(".config", engine.__name__)
    return engine


def render(engine, template):
    """Render designated template with designated engine."""
    config = engine.config.setup()
    return engine.config.render(config, template, VARIABLES)
