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
"""This module contains object that represents news.Source object."""

from newsapi.base import NewsObject

class Source(NewsObject):
    def __init__(self, id, name, description, url, category, language, country, urlsToLogos, sortBysAvailable, **kwargs):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        self.urlsToLogos = urlsToLogos
        self.sortBysAvailable = sortBysAvailable

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):

        Returns:
            newsapi.Source:
        """
        if not data:
            return None

        return Source(**data)