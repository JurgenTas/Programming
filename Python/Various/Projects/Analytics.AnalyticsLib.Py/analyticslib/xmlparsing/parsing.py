"""
:author: juergen.tas@triodos.com

XML parsing functionality
"""
from xml.etree.ElementTree import iterparse


def parse_large_xml_file(fname, npath):
    """
    Incrementally process large XML files; i.e. memory efficient
    :param fname: name of the xml file
    :param npath: xml node path
    :return: node generator object
    """
    path_parts = npath.split('/')
    data = iterparse(fname, ('start', 'end'))
    # skip the root element
    next(data)

    tag_stack = []
    elem_stack = []
    for event, elem in data:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass
