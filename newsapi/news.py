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
"""This module contains object that represents news.NewApi interface."""
from newsapi.articles import Articles
from newsapi.base import NewsObject
from newsapi.sources import Sources

class News(NewsObject):
    def __init__(self, apikey, url="https://newsapi.org/v1"):
        self.url = url
        self.apikey = apikey
    
    def load_sources(self):
        self.sources = Sources.load(self.url, self.apikey)
    
    def load_articles(self):
        self.articles = Articles.load(self.url, self.apikey, self.sources)

    def get_sources(self):
        return self.sources

    def get_articles(self):
        return self.articles

    def set_sources(self, sources):
        self.sources = sources
        
    def set_articles(self, articles):
        self.articles = articles

    