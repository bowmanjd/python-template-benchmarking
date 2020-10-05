"""Rendering for the chevron Mustache engine."""

import chevron

INCLUDES_RE = r"{{>\s+(\S+)\s*}}"
INCLUDES_EXT = ".mustache"


def compile_template(template_dict, template_name):
    """Compile template."""
    compiled = {
        template_name: tuple(chevron.tokenizer.tokenize(template_dict[template_name]))
        for template_name in template_dict
    }
    return compiled, template_name


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
