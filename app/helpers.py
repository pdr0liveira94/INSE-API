"""This module will encode and parse the query string params."""

import urllib.parse as urlparse
from urllib.parse import unquote
import sys
sys.modules['urlparse'] = urlparse
sys.modules['urllib'] = urlparse
from urlparse import parse_qs


def parse_query_params(query_string):

    """
        Function to parse the query parameter string.
    """
    print('string: ',query_string)
    query_params = dict(parse_qs(query_string))
    print('params: ', query_params)
    # Get the value from the list
    query_params = {k: v[0].replace('_', ' ') for k, v in query_params.items()}
    return query_params
