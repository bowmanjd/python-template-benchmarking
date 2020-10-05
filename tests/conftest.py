"""Configuration for pytest."""

import tplbench.dyno


def pytest_addoption(parser):
    """Add --engine argument to pytest command line."""
    parser.addoption(
        "--engine",
        action="append",
        default=[],
        help="templating engine to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    """Dynamically import designated engine."""
    if "engine" in metafunc.fixturenames:
        module_names = metafunc.config.getoption("engine")
        engines = [
            tplbench.dyno.import_engine(module_name) for module_name in module_names
        ]
        metafunc.parametrize("engine", engines)
