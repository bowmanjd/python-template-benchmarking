from pytemplates import dyno


def test_engine_config(engine):
    assert engine.config.render


def test_article(datadir, engine):
    template = "article.html"
    reference = (datadir / template).read_text()
    rendered = dyno.render(engine, template)
    assert reference.strip() == rendered.strip()
