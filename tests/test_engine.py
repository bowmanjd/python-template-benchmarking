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


def test_article(benchmark, datadir, engine):
    """Compare rendered article with reference article."""
    template = "article.html"
    reference = (datadir / template).read_text()
    rendered = benchmark(dyno.render_fresh, engine, template)
    print(rendered)
    formatted = standardize_html(rendered)
    assert reference == formatted


def test_article_reuse(benchmark, engine):
    """Benchmark only rendering, not setup."""
    config = dyno.render_setup(engine)
    template = "article.html"
    benchmark(dyno.render_only, engine, config, template)


def test_compile_and_render_article(benchmark, datadir, engine):
    """Compare rendered article with reference article."""
    template = "article.html"
    reference = (datadir / template).read_text()

    rendered = benchmark(dyno.compile_and_render, engine, template)
    print(rendered)
    formatted = standardize_html(rendered)
    assert reference == formatted


def test_render_compiled_article(benchmark, engine):
    """Benchmark only rendering, not compilation."""
    template = "article.html"
    compiled_template = dyno.precompile(engine, template)
    benchmark(dyno.render_compiled, engine, compiled_template)


def test_render_string_article(benchmark, engine):
    """Benchmark rendering from string."""
    template = "article.html"
    benchmark(dyno.render_string, engine, template)
