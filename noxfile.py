"""Task runner."""

import importlib.resources

import nox

from pytemplates import dyno, engines

nox.options.reuse_existing_virtualenvs = True

template_engines = [
    engine
    for engine in importlib.resources.contents(engines)
    if not engine.startswith("_")
]


@nox.session
@nox.parametrize("engine", template_engines)
def environments(session, engine):
    """Run pytest on each engine."""
    new_module = importlib.import_module(f"pytemplates.engines.{engine}")
    requirements = (
        importlib.resources.read_text(new_module, "requirements.txt")
        .strip()
        .split("\n")
    )
    session.install(".", "beautifulsoup4", "lxml", "pytest", "pytest-datadir", *requirements)
    session.run("pytest", "--engine", engine)
