"""Rendering for the chevron Mustache engine."""

import chevron

INCLUDES_RE = r"{{>\s+(\S+)\s*}}"
INCLUDES_EXT = ".mustache"


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


def compile_template(template_dict, template_name):
    """Compile template."""
    compiled = {
        template_name: tuple(chevron.tokenizer.tokenize(template_dict[template_name]))
        for template_name in template_dict
    }
    return compiled, template_name


# def compile_template(template, template_path, partials_dict=None):
#     """Compile template."""
#     if partials_dict is None:
#         partials_dict = {}
#     new_partials_dict = partials_dict.copy()
#     tokenized = tuple(chevron.tokenizer.tokenize(template))
#     for tag in tokenized:
#         if tag[0] == "partial" and tag[1] not in new_partials_dict:
#             partial_template = template_path.joinpath(f"{tag[1]}.mustache").read_text()
#             partial, partial_partials_dict = compile_template(
#                 partial_template, template_path, new_partials_dict
#             )
#             new_partials_dict[tag[1]] = partial
#             new_partials_dict = {**new_partials_dict, **partial_partials_dict}
#
#     return (tokenized, new_partials_dict)


def render_compiled(compiled, variables):
    """Render from compiled template with interpolated variables."""
    template_dict, template_name = compiled
    return chevron.render(
        template_dict[template_name], variables, partials_dict=template_dict
    )


def render_from_file(template_file, variables):
    """Render from template string with interpolated variables."""
    return chevron.render(
        template_file.read_text(), variables, partials_path=str(template_file.parent)
    )
