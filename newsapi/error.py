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
"""This module contains object that represents News Errors."""

class NewsError(Exception):
    """This object represents a newsapi Error."""

    def __init__(self, message):
        """
        Args:
            message (str):

        Returns:

        """
        super(NewsError, self).__init__()
        self.message = message

    def __str__(self):
        return '%s' % (self.message)

class Unauthorized(NewsError):

    def __init__(self):
        super(Unauthorized, self).__init__('Unauthorized')