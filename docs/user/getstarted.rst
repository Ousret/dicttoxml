Installation
============

The dicttoxml module is [published on the Python Package Index](https://pypi.python.org/pypi/dicttoxml2), so you can install it using `pip`.

    pip install dicttoxml2

That should be all you need to do.

Basic Usage
===========

Once installed, import the library into your script and convert a dict into xml by running the `dicttoxml` function:

    >>> import dicttoxml2
    >>> xml = dicttoxml2.dicttoxml(some_dict)

Alternately, you can import the `dicttoxml()` function from the library.

    >>> from dicttoxml2 import dicttoxml
    >>> xml = dicttoxml(some_dict)

That's it!

