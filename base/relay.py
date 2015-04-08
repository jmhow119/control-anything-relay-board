#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author(s)
---------
John M. Howard

Created On
----------
03-23-15

Purpose
-------
Defines the abstract functionality and attributes
for Control Anythin relays

Class(es)
---------
Relay

Function(s)
-----------

Requirements
------------

Platform
--------
OS X, Linux
"""


class Relay(object):
    """
    """

    def __init__(self, i):
        """
        """
        self.relay_number = i
        self._is_on = None

    def __repr__(self):
        return "control anything relay number %s" % self.relay_number

    def status(self):
        return self._is_on
