Dictionary to XML
=================

Converts a Python dictionary or other native data type into a valid XML string. 
This is a fork that support Python 3.9 and forward versions and drop all EOL (<=3.6) versions altogether.
It is mostly backward-compatible, act as a drop-in replacement.

Installation
============

**This module should work in Python 3.7+.**
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

Author
======

* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com](mailto:ryan@quandyfactory.com)
* Repository: [http://github.com/quandyfactory/dicttoxml](http://github.com/quandyfactory/dicttoxml)

Maintainer
==========

* Author: Ahmed TAHRI
* Email: [ahmed.tahri@cloudnursery.dev](mailto:ahmed.tahri@cloudnursery.dev)
* Repository: [http://github.com/Ousret/dicttoxml](http://github.com/Ousret/dicttoxml)

Copyright and Licence
=====================

Copyright 2012 by Ryan McGreal. 

Released under the GNU General Public Licence, Version 2:  
<http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>

