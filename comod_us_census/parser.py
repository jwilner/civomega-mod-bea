"""
Must define three methods:

* answer_pattern(pattern, args)
* render_answer_html(answer_data)
* render_answer_json(answer_data)
"""
import requests

from comod_us_census import patterns, handlers

import json
from django.template import loader, Context


PATTERN_HANDLERS = \
    {patterns.PLACE_YEAR_POPULATION: handlers.query_place_year_population,
     patterns.PLACE_POPULATION: handlers.query_place_year_population}

############################################################
# Pattern-dependent behavior


def answer_pattern(pattern, args):
    """
    Returns a `dict` representing the answer to the given
    pattern & pattern args.

    'plaintxt' should always be a returned field

    """
    if pattern not in patterns.PATTERNS:
        return None

    handler = PATTERN_HANDLERS[pattern]
    session = requests.Session()

    return {'plaintxt': '', "results": handler(session, *args)}

############################################################
# Applicable module-wide


def render_answer_html(answer_data):
    template = loader.get_template('comod_us_census/base_template.html')
    return template.render(Context(answer_data))


def render_answer_json(answer_data):
    return json.dumps(answer_data)
