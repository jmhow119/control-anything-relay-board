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

from relay import Relay


class RelayBoard(object):
    """
    """

    def __init__(self, number_of_relays):
        """
        """
        self._number_of_relays = number_of_relays
        self.objid_2_obj = {}

    def __repr__(self):
        pass

    def __getitem__(self, index):
        return self.objid_2_obj[index]

    def _load_relays(self):

        for i in self._number_of_relays:
            self.objid_2_obj[i] = Relay(i)

