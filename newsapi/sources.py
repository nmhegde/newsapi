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
"""This module contains object that represents news.Sources."""

from base import NewsObject
from newsapi.utils import headers
from newsapi.utils import request
from source import Source

class Sources(NewsObject):

    @staticmethod
    def load(host, apikey):
        url = host + '/sources?language=en' + '&apiKey=' + apikey
        return Sources.de_json(request.get(url, headers.get()))

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):

        Returns:
            list of newsapi.Sources:
        """
        if not data:
            return None

        sources = []
        for strjson in data['sources']:
            sources.append(Source.de_json(strjson))
        return sources
