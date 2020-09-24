"""Testing template engines."""

from bs4 import BeautifulSoup

from pytemplates import dyno


def standardize_html(html):
    """Clean and format html for consistency."""
    cleaned = html.replace(".  ", ". ").replace("  ", "").replace("\n", "")
    parsed = BeautifulSoup(cleaned, "lxml").prettify().strip()
    return parsed


def test_engine_config(engine):
    """Ensure that config is created."""
    assert engine.config.render


def test_article(datadir, engine):
    """Compare rendered article with reference article."""
    template = "article.html"
    reference = (datadir / template).read_text()
    rendered = dyno.render(engine, template)
    print(rendered)
    formatted = standardize_html(rendered)
    assert reference == formatted
