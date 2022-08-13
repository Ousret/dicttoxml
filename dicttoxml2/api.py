from logging import getLogger
from typing import Callable, Any, List

from .converters import convert
from .utils import default_item_func


logger = getLogger("dicttoxml")


def dicttoxml(obj: Any, root: bool = True, custom_root: str = 'root', ids: bool = False, attr_type: bool = True,
              item_func: Callable[[Any], str] = default_item_func, cdata: bool = False, fold_list: bool = True) -> bytes:
    """Converts a python object into XML.
    Arguments:
    - root specifies whether the output is wrapped in an XML root element
      Default is True
    - custom_root allows you to specify a custom root element.
      Default is 'root'
    - ids specifies whether elements get unique ids.
      Default is False
    - attr_type specifies whether elements get a data type attribute.
      Default is True
    - item_func specifies what function should generate the element name for
      items in a list.
      Default is 'item'
    - cdata specifies whether string values should be wrapped in CDATA sections.
      Default is False
    - fold_list when using the option fold_list=False the parameter item_func is ignored.
      In case of nested lists, all list entries will use the same parent dictionary name as item name.
      Default is True
    """
    logger.debug('Inside dicttoxml(): type(obj) is: "%s", obj="%s"' % (type(obj).__name__, obj))
    output: List[str] = []

    if root:
        output.append('<?xml version="1.0" encoding="UTF-8" ?>')
        output.append(
            f"<{custom_root}>{convert(obj, ids, attr_type, item_func, cdata, parent=custom_root, fold_list=fold_list)}</{custom_root}>"
        )
    else:
        output.append(convert(obj, ids, attr_type, item_func, cdata, parent='', fold_list=fold_list))

    return ''.join(output).encode('utf-8')
