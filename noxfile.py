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


def setup(session, engine):
    """Setup sessions."""
    new_module = importlib.import_module(f"pytemplates.engines.{engine}")
    requirements = (
        importlib.resources.read_text(new_module, "requirements.txt")
        .strip()
        .split("\n")
    )
    session.install(
        ".", "beautifulsoup4", "lxml", "pytest", "pytest-datadir", "pytest-benchmark"
    )
    session.install(*requirements)


@nox.session
@nox.parametrize("engine", template_engines, ids=template_engines)
def bench(session, engine):
    """Test and benchmark the designated templating engine."""
    setup(session, engine)
    session.run("pytest", "--engine", engine, "--benchmark-columns=ops")


@nox.session
@nox.parametrize("engine", template_engines, ids=template_engines)
def nobench(session, engine):
    """Test and benchmark the designated templating engine."""
    setup(session, engine)
    session.run("pytest", "--engine", engine, "--benchmark-disable")
