"""Package configuration."""
from setuptools import find_packages, setup

setup(
    name="tplbench",
    version="0.1.0",
    entry_points={"console_scripts": ["ditto=tplbench.ditto:run"]},
    install_requires=["nox"],
    packages=find_packages(),
)
