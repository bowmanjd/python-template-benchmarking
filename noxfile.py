"""Task runner."""

import importlib.resources
from pathlib import Path
import sys

import nox

nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["bench"]

sys.path = list(dict.fromkeys(("", *sys.path)))

TEMPLATE_ENGINES = [
    engine
    for engine in importlib.resources.contents("tplbench.engines")
    if not engine.startswith("_")
]


def setup(session, engine):
    """Setup sessions."""
    new_module = importlib.import_module(f"tplbench.engines.{engine}")
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
@nox.parametrize("engine", TEMPLATE_ENGINES, ids=TEMPLATE_ENGINES)
def bench(session, engine):
    """Test and benchmark the designated templating engine."""
    Path("benchmarks").mkdir(exist_ok=True)
    setup(session, engine)
    session.run(
        "pytest",
        "--engine",
        engine,
        "--benchmark-columns=ops",
        "--benchmark-name=short",
        f"--benchmark-json=benchmarks/{engine}.json",
    )


@nox.session
@nox.parametrize("engine", TEMPLATE_ENGINES, ids=TEMPLATE_ENGINES)
def nobench(session, engine):
    """Test and benchmark the designated templating engine."""
    setup(session, engine)
    session.run("pytest", "--engine", engine, "--benchmark-disable")
