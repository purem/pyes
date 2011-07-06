#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alberto Paro'

class HighLighter:
    """
    This object manage the highlighting
    """
    def __init__(self, pre_tags = None, post_tags = None, fields = None, fragment_size = None, number_of_fragments = None, fragment_offset = None):
        self.pre_tags = pre_tags
        self.post_tags = post_tags
        self.fields = fields or {}
        self.fragment_size = fragment_size
        self.fragment_offset = fragment_offset
        self.number_of_fragments = number_of_fragments
    
    def add_field(self, name, fragment_size=150, number_of_fragments=3, fragment_offset=None):
        """
        Add a field to Highlinghter
        """
        data = {}
        if fragment_size:
            data['fragment_size'] = fragment_size
        if number_of_fragments is not None:
            data['number_of_fragments'] = number_of_fragments
        if fragment_offset is not None:
            data['fragment_offset'] = fragment_offset            
        self.fields[name] = data

    def serialize(self):
        res = {}
        if self.pre_tags:
            res["pre_tags"] = self.pre_tags
        if self.post_tags:
            res["post_tags"] = self.post_tags
        if self.fragment_size:
            res["fragment_size"] = self.fragment_size
        if self.number_of_fragments:
            res["number_of_fragments"] = self.number_of_fragments
        if self.fragment_offset:
            res["fragment_offset"] = self.fragment_offset
        if self.fields:
            res["fields"] = self.fields
        else:
            res["fields"] = {"_all" : {}}
        return res
