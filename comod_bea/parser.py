"""
Must define three methods:

* answer_pattern(pattern, args)
* render_answer_html(answer_data)
* render_answer_json(answer_data)
"""
import os

from comod_bea import handlers

import json
from django.template import loader, Context

# Pattern-dependent behavior
############################################################


def answer_pattern(pattern, args):

    """
    Returns a `dict` representing the answer to the given
    pattern & pattern args.

    'plaintxt' should always be a returned field

    """
    if pattern not in handlers.PATTERN_HANDLERS:
        return None

    handler, kwargs, template = handlers.PATTERN_HANDLERS[pattern]

    session = handlers.BeaSession()

    try:
        results = handler(session, *args, **kwargs)
    except session.SESSION_EXCEPTIONS as e:
        raise e  # return None doesn't seem to work here despite example.

    return {'plaintxt': '', "template": template, "results": results}

############################################################
# Applicable module-wide


def render_answer_html(answer_data):
    print answer_data
    results = answer_data["results"]
    template = answer_data["template"]
    template = loader.get_template(os.path.join('comod_bea', template))
    return template.render(Context(results))


def render_answer_json(answer_data):
    return json.dumps(answer_data)
