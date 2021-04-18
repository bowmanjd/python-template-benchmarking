"""Task runner."""

import contextlib
import importlib.resources
from pathlib import Path
import sys

import nox

nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["test"]

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
def templates(session):
    """Create/update templates."""
    session.install(".", "beautifulsoup4", "lxml", "mimesis")
    session.run("ditto")


@nox.session
@nox.parametrize("engine", TEMPLATE_ENGINES, ids=TEMPLATE_ENGINES)
def test(session, engine):
    """Test and benchmark the designated templating engine."""
    nobench = False
    if session.posargs:
        args = session.posargs[:]
        with contextlib.suppress(ValueError):
            # Consume nobench argument, set nobench flag if present
            nobench = bool(args.pop(args.index("--nobench")))

    if nobench:
        pytest_args = ["--benchmark-disable"]
    else:
        Path("benchmarks").mkdir(exist_ok=True)
        pytest_args = [
            "--benchmark-columns=ops",
            f"--benchmark-json=benchmarks/{engine}.json",
        ]

    setup(session, engine)

    session.run("pytest", "--engine", engine, *pytest_args)
