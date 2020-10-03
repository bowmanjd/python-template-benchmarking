"""Rendering for Liquidpy engine."""


from liquid import Liquid

INCLUDES_RE = r"{%\s*(?:extends|include)\s+['\"]([^'\"]+)['\"]\s*%}"


def compile_template(template_dict, template_name):
    """Compile template."""
    template_path = "pytemplates/engines/liquidpy/"
    template = Liquid(
        template_dict[template_name], liquid_config={"extends_dir": [template_path]},
    )
    return template


def render_compiled(compiled, variables):
    """Render from compiled template with interpolated variables."""
    return compiled.render(**variables)


def render_from_file(template_file, variables):
    """Render from template string with interpolated variables."""
    template = Liquid(str(template_file))
    return template.render(**variables)
