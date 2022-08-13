from datetime import datetime
from random import randint
from numbers import Number
from html import escape
from secrets import token_hex
from typing import Dict
from xml.dom.minidom import parseString
from logging import getLogger, DEBUG, ERROR, FileHandler, StreamHandler


logger = getLogger("dicttoxml")


def set_debug(debug: bool = True, filename: str = 'dicttoxml.log'):
    """Kept for BC reasons."""
    if debug:
        logger.setLevel(DEBUG)

        if len(logger.handlers) == 1:
            logger.addHandler(
                FileHandler(filename)
            )
            logger.addHandler(
                StreamHandler()
            )

        logger.debug(f'\nLogging session starts: {datetime.now().isoformat()}')
    else:
        logger.debug('Debug mode is off.')
        logger.setLevel(ERROR)


def make_id(element, start=100000, end=999999):
    """Returns a random integer. Kept for BC reasons."""
    return f"{element}_{randint(start, end)}"


def get_unique_id(element):
    """Returns a unique id for a given element"""
    return f"{element}_{token_hex(16)}"


def get_xml_type(val):
    """Returns the data type for the xml type attribute"""
    if val is None:
        return 'null'
    if isinstance(val, (str, int, float, bool, dict, list)):
        return type(val).__name__
    if isinstance(val, Number):
        return 'number'

    return type(val).__name__


def escape_xml(s: str):
    """Kept for BC reasons"""
    return escape(s) if isinstance(s, str) else s


def make_attrstring(attr):
    """Returns an attribute string in the form key="val" """
    attrstring = ' '.join(['%s="%s"' % (k, v) for k, v in attr.items()])
    return '%s%s' % (' ' if attrstring != '' else '', attrstring)


def key_is_valid_xml(key):
    """Checks that a key is a valid XML name"""
    logger.debug('Inside key_is_valid_xml(). Testing "%s"' % (key))
    test_xml = '<?xml version="1.0" encoding="UTF-8" ?><%s>foo</%s>' % (key, key)
    try:
        parseString(test_xml)
        return True
    except:  # minidom does not implement exceptions well
        return False


def make_valid_xml_name(key: str, attr: Dict[str, str]):
    """Tests an XML name and fixes it if invalid"""
    logger.debug('Inside make_valid_xml_name(). Testing key "%s" with attr "%s"' % (key, attr))
    key = escape_xml(key)

    # pass through if key is already valid
    if key_is_valid_xml(key):
        return key, attr

    # prepend a lowercase n if the key is numeric
    if isinstance(key, int) or key.isdigit():
        return 'n%s' % (key), attr

    # replace spaces with underscores if that fixes the problem
    if key_is_valid_xml(key.replace(' ', '_')):
        return key.replace(' ', '_'), attr

    # key is still invalid - move it into a name attribute
    attr['name'] = key
    key = 'key'
    return key, attr


def wrap_cdata(s):
    """Wraps a string into CDATA sections"""
    s = str(s).replace(']]>', ']]]]><![CDATA[>')
    return '<![CDATA[' + s + ']]>'


def default_item_func(parent) -> str:
    return 'item'


