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
from newsapi.article import Article
from newsapi.utils import headers
from newsapi.utils import request
from source import Source

class Articles(NewsObject):

    def __init__(self, source, sortBy, articles):
        self.source = source
        self.sortBy = sortBy
        self.articles = articles

    @staticmethod
    def load(host, apikey, sources):
        articles = []
        for source in sources:
            for sortBy in source.sortBysAvailable:
                url = host + '/articles'
                url += '?source=' + source.id
                url += '&sortBy=' + sortBy
                url += '&apiKey=' + apikey
                articles.append(Articles.de_json(request.get(url, headers.get())))

        return articles

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):

        Returns:
            list of newsapi.Articles:
        """
        if not data:
            return None

        source = data['source']
        sortBy = data['sortBy']
        articles = []
        for strjson in data['articles']:
            articles.append(Article.de_json(strjson))

        return Articles(source, sortBy, articles)