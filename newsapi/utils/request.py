#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A library that provides a Python interface to the newapi.org API
# Copyright (C) 2016
# Naveen Sanmane & Nikhil Hegde
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains get methods."""

import functools
import json
import socket
from ssl import SSLError

from future.moves.http.client import HTTPException
from future.moves.urllib.error import HTTPError, URLError
from future.moves.urllib.request import urlopen, urlretrieve, Request

def _parse(json_data):
    """Try and parse the JSON returned from newsapi.org or return an empty
    dictionary if there is any error.

    Args:
      url:
        urllib.urlopen object

    Returns:
      A JSON parsed as Python dict with results.
    """
    decoded_s = json_data.decode('utf-8')
    data = None
    try:
        data = json.loads(decoded_s)
    except ValueError as error:
        pass

    return data


def get(url, headers=None):
    """Request an URL.
    Args:
      url:
        The web location we want to retrieve.

    Returns:
      A JSON object.
    """

    print(url)
    request = Request(url, headers=headers)
    result = urlopen(request).read()

    return _parse(result)
