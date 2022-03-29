Revision History
================

Version 2.0.0
-------------

* Release Date: 2022-03-28
* Changes:
    * The immediate priority is to get things up and running without BC-Break (as possible) 
    * Mostly backward-compatible
    * Removed support for EOL Python 2.7, 3.5 and 3.6
    * Added support for Python 3.9 and forward
    * Add separate `CHANGELOG.md`
    * Updated README.markdown
    * Lowered logging entries to strict `debug`
    * Major package restructuring while keeping BC on what is expected to be public API
    * Unique node identifier now uses `token_hex` from **secrets** instead of `randint`

Version 1.7.4
-------------

* Release Date: 2016-07-08
* Changes:
    * Fixed [bug #46](https://github.com/quandyfactory/dicttoxml/issues/46) on github. Thanks to [robbincatz](https://github.com/robbincatz) for identifying and reporting the issue.

Version 1.7.3
-------------

* Release Date: 2016-07-07
* Changes:
    * Updated README.markdown

Version 1.7.2
-------------

* Release Date: 2016-07-07
* Changes:
    * XML-encodes values to avoid XML injection. Big thanks to [thomaskonrad](https://github.com/thomaskonrad) on Github, via [issue #41](https://github.com/quandyfactory/dicttoxml/issues/41).

Version 1.7.1
-------------

* Release Date: 2016-07-06
* Changes:
    * Added ability to wrap values with CDATA. Big thanks to [LeviTaule](https://github.com/LeviTaule) on Github, via [pull request #45](https://github.com/quandyfactory/dicttoxml/pull/45/files).

Version 1.7
-----------

* Release Date: 2016-06-13
* Changes:
    * First of all, sorry for such a log delay between releases! I have not been a responsible steward of this project and I aim to change that from now on. This is the first in a series of updates I will be pushing over the next couple of months to get caught up on the backlog of issues and pull requests.
    * Added ability to customize `list` and `dict` item names via a function argument passed into the `dicttoxml()` function. Customizeable item name function takes the item's parent element as an argument. Big thanks to [viktor-zireael](https://github.com/viktor-zireael) on Github, via [pull request #40](https://github.com/quandyfactory/dicttoxml/pull/40/files).
    * Updated code style to more closely follow PEP8.

Version 1.6.6
-------------

* Release Date: 2015-04-09
* Changes:
    * PyPi does not want to upload version 1.6.5. It's returning an `Upload failed (500): Internal Server Error` message when I try to upload the code. I'm incrementing the version by one and reinstalling it to see if that fixes the issue.

Version 1.6.5
-------------

* Release Date: 2015-04-09
* Changes:
    * Fixed [issue #37](https://github.com/quandyfactory/dicttoxml/issues/37), elements with boolean values were getting a "number" type attribute. The issue was that `isinstance(True, numbers.Number)` returns `True`. I modified the `get_xml_type()` function to test for `boolean` before testing for `numbers.Number`. Thanks to [badsequel](https://github.com/badsequel) for identifying and reporting the issue.

Version 1.6.4
-------------

* Release Date: 2015-03-11
* Changes:
    * Fixed [issue #36](https://github.com/quandyfactory/dicttoxml/issues/36), logging was throwing an UnicodeDecodeError on non-ASCII characters in dictionary values. Thanks to [beef9999](https://github.com/beef9999) for identifying and reporting the issue.

Version 1.6.3
-------------

* Release Date: 2015-03-05
* Changes:
    * Updated README.markdown to reflect changes made in v. 1.6.2.

Version 1.6.2
-------------

* Release Date: 2015-03-05
* Changes:
    * Fixed [issue #35](https://github.com/quandyfactory/dicttoxml/issues/35), dicttoxml fails to identify a `decimal.Decimal` as a number. This is done by replacing `type(val).__name__ in ('int', 'long')` with the more generic `isinstance(val, number.Number)`. Thanks to [jmagnusson](https://github.com/jmagnusson) for finding and fixing the error.

Version 1.6.1
-------------

* Release Date: 2015-03-05
* Changes:
    * Merged [pull request #34](https://github.com/quandyfactory/dicttoxml/pull/34), fix misleading TypeError in `convert_dict()`. Thanks to [jmagnusson](https://github.com/jmagnusson) for finding and fixing the error.

Version 1.6.0
-------------

* Release Date: 2015-02-23
* Changes:
    * Fixed [issue #32](https://github.com/quandyfactory/dicttoxml/issues/32), duplication in test for list-like data types.

Version 1.5.9
-------------

* Release Date: 2015-02-23
* Changes:
    * Merged [pull request #33](https://github.com/quandyfactory/dicttoxml/pull/33) to replace invocations of `logging` with `LOG`. Thanks to [mfriedenhagen ](https://github.com/mfriedenhagen) for identifying the issue with the logger, and to [seyhuns](https://github.com/seyhuns) for supplying a pull request that could be merged automatically.

Version 1.5.8
-------------

* Release Date: 2015-01-06
* Changes:
    * Fixed [issue #30](https://github.com/quandyfactory/dicttoxml/issues/30) via [pull request #31](https://github.com/quandyfactory/dicttoxml/pull/31). Thanks to [isaac-councill](https://github.com/isaac-councill) for identifying the issue and providing a fix.

Version 1.5.7
-------------

* Release Date: 2014-12-09
* Changes:
    * Fixed [issue #29](https://github.com/quandyfactory/dicttoxml/issues/29). Thanks to [birdsarah](https://github.com/birdsarah) for identifying this performance issue and providing a fix.

Version 1.5.6
-------------

* Release Date: 2014-08-18
* Changes:
    * Fixed [issue #24](https://github.com/quandyfactory/dicttoxml/issues/24). Thanks to [gdude2002](https://github.com/gdude2002) for identifying the issue.
    * Abstracted all XML validity tests to a single function `make_valid_xml_name(key, attr)`

Version 1.5.5
-------------

* Release Date: 2014-06-16
* Changes:
    * Fixed [issue #21](https://github.com/quandyfactory/dicttoxml/pull/21). Thanks to [lichenbo](https://github.com/lichenbo) for identifying the issue and providing a fix.
    * Abstracted setting XML type attribute into a function, `get_xml_type()`.
    * Standardized variable names inside functions (e.g. `k` -> `key`, `v` -> `val`).
    * Cleaned up README so it works as both Markdown (for github) and ReStructuredText (for PyPi)

Version 1.5.4
-------------

* Release Date: 2014-06-03
* Changes:
    * Fixed [issue #20](https://github.com/quandyfactory/dicttoxml/issues/20).  Thanks to [lichenbo](https://github.com/lichenbo) for identifying the issue and providing a fix.

Version 1.5.3
-------------

* Release Date: 2014-06-08
* Changes:
    * Minor updates to README.markdown

Version 1.5.2
-------------

* Release Date: 2014-06-03
* Changes:
    * Minor updates to README.markdown

Version 1.5.1
-------------

* Release Date: 2014-06-03
* Changes:
    * Minor updates to README.markdown

Version 1.5
-----------

* Release Date: 2014-06-03
* Changes:
    * Added ability to set a custom root element, as per [issue #18](https://github.com/quandyfactory/dicttoxml/issues/18) by [murielsilveira](https://github.com/murielsilveira).

Version 1.4
-----------

* Release Date: 2014-06-03
* Changes:
    * Element type attribute made optional via pull request from [gauravub](https://github.com/gauravub] to resolve [issue #17](https://github.com/quandyfactory/dicttoxml/pull/17).

Version 1.3.7
-------------

* Release Date: 2014-04-21
* Changes:
    * Updated `MANIFEST.in` and `setup.py` so the licence and readme are properly included in the distribution.

Version 1.3.6
-------------

* Release Date: 2014-04-21
* Changes:
    * Added `MANIFEST.in` to include the `LICENCE.txt` and `README.markdown` files in the distribution, as per [issue #15](https://github.com/quandyfactory/dicttoxml/issues/15).

Version 1.3.5
-------------

* Release Date: 2014-04-14
* Changes:
    * `dicttoxml()` accepts `[None]` as a parameter and returns a valid XML object, as per [issue #13](https://github.com/quandyfactory/dicttoxml/issues/13).

Version 1.3.4
-------------

* Release Date: 2014-04-14
* Changes:
    * `dicttoxml()` now accepts `None` as a parameter and returns a valid XML object, as per [issue #13](https://github.com/quandyfactory/dicttoxml/issues/13).

Version 1.3.3
-------------

* Release Date: 2014-04-14
* Changes:
    * Automatically converts spaces in key names to underscores, as per [issue #12](https://github.com/quandyfactory/dicttoxml/pull/12).

Version 1.3.2
-------------

* Release Date: 2014-04-14
* Changes:
    * Added convert_none() function to convert a null value into XML
    * Added `key_is_valid_xml()` function to test if a key is valid XML
    * Updated `convert_kv()`, `convert_bool()` and `convert_none()` functions to test whether the key is a valid XML name and, if it is not, to render it as `<key name="{invalidname}">value</key>`. This addresses [issue 10](https://github.com/quandyfactory/dicttoxml/issues/10).

Version 1.3.1
-------------

* Release Date: 2013-07-12
* Changes:
    * Updated README to note support for dict-like and iterable objects.

Version 1.3
-----------

* Release Date: 2013-07-12
* Changes:
    * changed test for dict type from `type(x)=dict` to `isinstance(x,dict)` to include dict-like subclases derived from dict, as per [issue 9](https://github.com/quandyfactory/dicttoxml/issues/9).
    * Added test for `isinstance(x,collections.Iterable)` to test for list, set, tuple to accommodate iterable objects, as per [issue 9](https://github.com/quandyfactory/dicttoxml/issues/9).

Version 1.2
-----------

* Release Date: 2013-07-11
* Changes:
    * Fixed typo in convert_list() exception raise as per [issue 8](https://github.com/quandyfactory/dicttoxml/issues/8).

Version 1.1.2
-------------

* Release Date: 2013-05-06
* Changes:
    * Renamed github repo from dict2xml to dicttoxml to match PyPI name.

Version 1.1.1
-------------

* Release Date: 2013-05-06
* Changes:
    * Fixed README.markdown

Version 1.1
-----------

* Release Date: 2013-05-06
* Changes:
    * Added an optional `ids` argument to give each element a unique, randomly generated id attribute.
    * All elements now inlcude a `type` attribute.
    * Updated readme with more examples and Python 3 compatible syntax.
    * Thanks to [cpetz](https://github.com/cpetz) for [suggesting](https://github.com/quandyfactory/dicttoxml/issues/7) this feature.

Verson 1.0
----------

* Release Date: 2013-03-04
* Changes:
    * Replaced debug function with `logging` module.
    * Converted code to work in Python 2.6+ and Python 3.
    * Fixed unresolved isoformat reference in `convert_list`.
    * Bug thanks to [regisd](https://github.com/regisd) for forking code and making several important fixes!

Version 0.9.1
-------------

* Release Date: 2013-03-03
* Changes:
    * Merged [pull request](https://github.com/quandyfactory/dicttoxml/pull/5) from [regisd](https://github.com/regisd) to fix [issue #5](https://github.com/quandyfactory/dicttoxml/issues/5), in which special XML characters were not being escaped properly.

Version 0.9
-----------

* Release Date: 2013-02-27
* Changes:
    * Added support for tuples.

Version 0.8
-----------

* Release Date: 2013-02-23
* Changes:
    * Changed name to dicttoxml and published to the Python Package Index (PyPI).

Version 0.7
-----------

* Release Date: 2012-09-12
* Changes:
    * Fixed [issue #4](https://github.com/quandyfactory/dicttoxml/issues/4) - thanks to PaulMdx for finding it and suggesting a fix.

Version 0.6
-----------

* Release Date: 2012-07-13
* Changes: 
    * Merged pull request from [0902horn](https://github.com/0902horn/dicttoxml) on github to escape special XML characters.

Version 0.5
-----------

* Release Date: 2012-02-28
* Changes: 
    * Added support for datetime objects (converts them into ISO format strings) and sets (converts them into lists).
    * Fixed [bug 2](https://github.com/quandyfactory/dicttoxml/issues/2) by raising an exception on unsupported data types.

Version 0.4
-----------

* Release Date: 2012-01-26
* Changes: 
    * Added optional `root` argument (default `True`) on whether to wrap the generated XML in an XML declaration and a root element.
    * Added ability to convert a root object of other data types - int, float, str, unicode, list - as well as dict.
    * Corrected `license` attribute in `setup.py`.
    * Renamed `notify()` function to `debug_notify()` and made it more comprehensive.

Version 0.3
-----------

* Release Date: 2012-01-24
* Changes: 
    * Fixed inconsistent str/string attributes.

Version 0.2
-----------

* Release Date: 2012-01-24
* Changes: 
    * Fixed bug in list items.
    * Added element attribute with data type.

Version 0.1
-----------

* Release Date: 2012-01-24
* Changes: 
    * First commit.