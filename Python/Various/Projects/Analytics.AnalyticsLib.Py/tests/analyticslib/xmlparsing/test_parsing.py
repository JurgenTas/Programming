"""
:author: juergen.tas@triodos.com

Implements unit tests for parse.py
"""
# -*- coding: utf-8 -*-

import os

from analyticslib.xmlparsing.parsing import parse_large_xml_file

FILENAME = os.path.join(os.path.dirname(__file__), 'test.xml')


def test_parse_large_xml_file():
    """Test function for parse_large_xml_file function"""
    file = FILENAME
    npath = 'channel/item'
    data = parse_large_xml_file(file, npath)
    lst = [item.findtext('title') for item in data]
    expected_result = 25
    result = len(lst)
    assert expected_result == result
