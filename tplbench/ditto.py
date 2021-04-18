"""Generate mock templates."""

# header
# footer
# var
# loop(list)
# paragraph
#

import re

from mimesis import Generic

GENERATOR = Generic()

BRACE_RE = re.compile(r"{([^}]+)}")
SENTENCE_RE = re.compile(r"(?:[.!?]\"?)(\s+)(?=[A-Z])")


def escape_braces(text, pattern=BRACE_RE):
    escaped = pattern.sub(r"{{\1}}", text)
    return escaped


def randomly_segment(string, quantity, separator):
    """Segment string into quantity of segments, split by separator."""
    for match in separator.finditer(string):
        
    upper = len(string)


def transform_random_items(templates, items, quantity):
    """Transform random items in a list with the given template or template list."""
    upper = len(items)
    new_items = items.copy()
    item_indexes = GENERATOR.numbers.integers(1, upper, quantity)
    if isinstance(templates, str):
        single_template = escape_braces(templates)
    else:
        single_template = None
        templates_collection = tuple(templates)
        iter_templates = iter(templates_collection)

    for index in item_indexes:
        try:
            template = single_template or escape_braces(next(iter_templates))
        except StopIteration:
            iter_templates = iter(templates_collection)
            template = escape_braces(next(iter_templates))
        new_items[index] = template.format(new_items[index])
    return new_items


def paragraphs(
    paragraph_quantity, variable_quantity, total_sentences, variable_template
):
    """Generate the desired number of paragraphs with inserted variables."""
    text = GENERATOR.text.text(total_sentences)
    words = text.split(" ")
    variables = (
        escape_braces(variable_template).replace("var", "{}").format(f"var{num}")
        for num in range(variable_quantity)
    )
    wedged = transform_random_items("{{{{ {} }}}} ", words, variable_quantity, 1)
    sentences = " ".join(wedged).split(". ")
    linebroken = inserts("\n\n", sentences, paragraph_quantity)
    return ". ".join(linebroken)


def run():
    """Run from command line."""
    print(paragraphs(50, 400, 300, "{{ var }}"))
