"""Rendering for the chevron Mustache engine."""

from pathlib import Path

import chevron


def setup():
    """Initial environment setup."""
    config = {}
    config["path"] = Path("pytemplates/engines/chevron/")
    return config


def render(config, template_name, variables):
    """Render template with interpolated variables."""
    with (config["path"] / template_name).open() as template:
        rendered = chevron.render(
            template, variables, partials_path=str(config["path"])
        )
    return rendered


def compile_template(template, template_path, partials_dict=None):
    """Compile template."""
    if partials_dict is None:
        partials_dict = {}
    new_partials_dict = partials_dict.copy()
    tokenized = tuple(chevron.tokenizer.tokenize(template))
    for tag in tokenized:
        if tag[0] == "partial" and tag[1] not in new_partials_dict:
            partial_template = template_path.joinpath(f"{tag[1]}.mustache").read_text()
            partial, partial_partials_dict = compile_template(
                partial_template, template_path, new_partials_dict
            )
            new_partials_dict[tag[1]] = partial
            new_partials_dict = {**new_partials_dict, **partial_partials_dict}

    return (tokenized, new_partials_dict)


def render_compiled(compiled, variables):
    """Render from compiled template with interpolated variables."""
    template, partials_dict = compiled
    return chevron.render(template, variables, partials_dict=partials_dict)


def render_string(template, template_path, variables):
    """Render from template string with interpolated variables."""
    return chevron.render(template, variables, partials_path=str(template_path))
