"""
Converts a Python dictionary or other native data type into a valid XML string.

Supports item :
(`int`, `float`, `long`, `decimal.Decimal`, `bool`, `str`, `unicode`, `datetime`, `none` and other number-like objects)
and collection (`list`, `set`, `tuple` and `dict`, as well as iterable and dict-like objects) data types,
with arbitrary nesting for the collections. Items with a `datetime` type are converted to ISO format strings.
Items with a `None` type become empty XML elements.

This module no longer work with Python < 3.7
All EOL versions (in Q1-2022) are dropped.
"""

from .api import dicttoxml
from .utils import set_debug
from .version import __version__, version

from logging import getLogger, NullHandler

__all__ = (
    "dicttoxml",
    "set_debug",
    "version",
    "__version__",
)

logger = getLogger("dicttoxml")
logger.addHandler(NullHandler())

LOG = logger  # Kept for BC-Reasons
