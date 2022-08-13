from datetime import datetime
from logging import getLogger
from collections.abc import Iterable
from numbers import Number
from typing import Any, Callable, Mapping, Dict

from .utils import get_unique_id, get_xml_type, make_valid_xml_name, make_attrstring, escape_xml, wrap_cdata


logger = getLogger("dicttoxml")


def convert(obj: Any, ids: bool, attr_type: bool, item_func: Callable[[Any], str], cdata: bool, fold_list: bool, parent: str = 'root'):
    """Routes the elements of an object to the right function to convert them
    based on their data type"""

    logger.debug('Inside convert(). obj type is: "%s", obj="%s"' % (type(obj).__name__, obj))

    item_name = item_func(parent)

    if obj is None:
        return convert_none(item_name, '', attr_type, cdata=cdata)

    if isinstance(obj, bool):
        return convert_bool(item_name, obj, attr_type, cdata=cdata)

    if isinstance(obj, (Number, str)):
        return convert_kv(item_name, obj, attr_type, cdata=cdata)

    if isinstance(obj, datetime):
        return convert_kv(item_name, obj.isoformat(), attr_type, cdata=cdata)

    if isinstance(obj, dict):
        return convert_dict(obj, ids, parent, attr_type, item_func, cdata=cdata, fold_list=fold_list)

    if isinstance(obj, Iterable):
        return convert_list(obj, ids, parent, attr_type, item_func, cdata=cdata, fold_list=fold_list)

    raise TypeError('Unsupported data type: %s (%s)' % (obj, type(obj).__name__))


def convert_dict(obj: Mapping, ids: bool, parent: str, attr_type: bool, item_func: Callable[[Any], str], cdata: bool, fold_list: bool):
    """Converts a dict into an XML string."""
    logger.debug('Inside convert_dict(): obj type is: "%s", obj="%s"' % (type(obj).__name__, obj))
    output = []

    item_name = item_func(parent)

    for key, val in obj.items():
        logger.debug('Looping inside convert_dict(): key="%s", val="%s", type(val)="%s"' % (key, val, type(val).__name__))

        attr = {} if not ids else {'id': '%s' % (get_unique_id(parent)) }

        key, attr = make_valid_xml_name(key, attr)

        if isinstance(val, bool):
            output.append(convert_bool(key, val, attr_type, attr, cdata))
        elif isinstance(val, (Number, str)):
            output.append(convert_kv(key, val, attr_type, attr, cdata))
        elif isinstance(val, datetime):
            output.append(convert_kv(key, val.isoformat(), attr_type, attr, cdata))

        elif isinstance(val, dict):
            if attr_type:
                attr['type'] = get_xml_type(val)
            output.append('<%s%s>%s</%s>' % (key, make_attrstring(attr), convert_dict(val, ids, key, attr_type, item_func, cdata, fold_list), key))

        elif isinstance(val, list):
            if attr_type:
                attr['type'] = get_xml_type(val)
            if fold_list:
                output.append('<%s%s>%s</%s>' % (
                    key,
                    make_attrstring(attr),
                    convert_list(val, ids, key, attr_type, item_func, cdata, fold_list),
                    key
                ))
            else:
                output.append(
                    convert_list(val, ids, key, attr_type, item_func, cdata, fold_list)
                )

        elif val is None:
            output.append(convert_none(key, val, attr_type, attr, cdata))

        else:
            raise TypeError('Unsupported data type: %s (%s)' % (val, type(val).__name__))

    return ''.join(output)


def convert_list(items: Iterable, ids: bool, parent: str, attr_type: bool, item_func: Callable[[Any], str], cdata: bool, fold_list: bool):
    """Converts a list into an XML string."""
    logger.debug('Inside convert_list()')
    output = []

    item_name = item_func(parent) if fold_list else parent

    if ids:
        this_id = get_unique_id(parent)

    for i, item in enumerate(items):
        logger.debug('Looping inside convert_list(): item="%s", item_name="%s", type="%s"' % (item, item_name, type(item).__name__))

        attr = {} if not ids else { 'id': '%s_%s' % (this_id, i + 1)}

        if isinstance(item, bool):
            output.append(convert_bool(item_name, item, attr_type, attr, cdata))
        elif isinstance(item, (Number, str)):
            output.append(convert_kv(item_name, item, attr_type, attr, cdata))
        elif isinstance(item, datetime):
            output.append(convert_kv(item_name, item.isoformat(), attr_type, attr, cdata))
        elif isinstance(item, dict):
            if not attr_type:
                output.append('<%s>%s</%s>' % (
                    item_name,
                    convert_dict(item, ids, parent, attr_type, item_func, cdata, fold_list),
                    item_name,
                )
                        )
            else:
                output.append('<%s type="dict">%s</%s>' % (
                    item_name,
                    convert_dict(item, ids, parent, attr_type, item_func, cdata, fold_list),
                    item_name,
                )
                        )

        elif isinstance(item, Iterable):
            if not attr_type:
                output.append('<%s %s>%s</%s>' % (
                    item_name, make_attrstring(attr),
                    convert_list(item, ids, item_name, attr_type, item_func, cdata, fold_list),
                    item_name,
                )
                        )
            else:
                output.append('<%s type="list"%s>%s</%s>' % (
                    item_name, make_attrstring(attr),
                    convert_list(item, ids, item_name, attr_type, item_func, cdata, fold_list),
                    item_name,
                )
                        )

        elif item is None:
            output.append(convert_none(item_name, None, attr_type, attr, cdata))

        else:
            raise TypeError('Unsupported data type: %s (%s)' % (item, type(item).__name__))

    return ''.join(output)


def convert_kv(key: str, val: Any, attr_type: bool, attr: Dict[str, str] = None, cdata: bool = False):
    """Converts a number or string into an XML element"""

    if attr is None:
        attr = {}

    logger.debug('Inside convert_kv(): key="%s", val="%s", type(val) is: "%s"' % (key, val, type(val).__name__))

    key, attr = make_valid_xml_name(key, attr)

    if attr_type:
        attr['type'] = get_xml_type(val)  # type: ignore

    attrstring = make_attrstring(attr)

    return '<%s%s>%s</%s>' % (
        key, attrstring,
        wrap_cdata(val) if cdata is True else escape_xml(val),
        key
    )


def convert_bool(key: str, val: Any, attr_type: bool, attr: Dict[str, str] = None, cdata: bool = False):
    """Converts a boolean into an XML element"""
    if attr is None:
        attr = {}

    logger.debug('Inside convert_bool(): key="%s", val="%s", type(val) is: "%s"' % (key, val, type(val).__name__))

    key, attr = make_valid_xml_name(key, attr)

    if attr_type:
        attr['type'] = get_xml_type(val)  # type: ignore

    attrstring = make_attrstring(attr)

    return '<%s%s>%s</%s>' % (
        key, attrstring,
        wrap_cdata(val) if cdata is True else str(val),
        key
    )


def convert_none(key: str, val: Any, attr_type: bool, attr: Dict[str, str] = None, cdata: bool = False):
    """Converts a null value into an XML element"""
    if attr is None:
        attr = {}

    logger.debug('Inside convert_none(): key="%s"' % (key))

    key, attr = make_valid_xml_name(key, attr)

    if attr_type:
        attr['type'] = get_xml_type(val)  # type: ignore

    attrstring = make_attrstring(attr)

    return '<%s%s></%s>' % (key, attrstring, key)
