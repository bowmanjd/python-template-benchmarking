"""Testing template engines."""

from bs4 import BeautifulSoup

from tplbench import dyno


def standardize_html(html):
    """Clean and format html for consistency."""
    cleaned = html.replace(".  ", ". ").replace("  ", "").replace("\n", "")
    parsed = BeautifulSoup(cleaned, "lxml").prettify().strip()
    return parsed


def test_compile_and_render_article(benchmark, datadir, engine):
    """Compare rendered article with reference article."""
    template = "article.html"
    reference = (datadir / template).read_text()
    rendered = benchmark(dyno.compile_and_render, engine, template)
    formatted = standardize_html(rendered)
    assert reference == formatted


def test_render_from_compiled_article(benchmark, engine):
    """Benchmark only rendering, not compilation."""
    template = "article.html"
    compiled_template = dyno.precompile(engine, template)
    benchmark(dyno.render_compiled, engine, compiled_template)


def test_render_from_file_article(benchmark, engine):
    """Benchmark rendering from string."""
    template = "article.html"
    benchmark(dyno.render_from_file, engine, template)
