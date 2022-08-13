import pytest
from collections import OrderedDict
from dicttoxml2 import dicttoxml


def test_with_cdata_dict() -> None:
    payload: dict = {'mylist': ['foo', 'bar', 'baz'], 'mydict': {'foo': 'bar', 'baz': 1}, 'ok': True}

    expected: bytes = b'<?xml version="1.0" encoding="UTF-8" ?><root><mylist type="list"><item type="str">' \
                      b'<![CDATA[foo]]></item><item type="str"><![CDATA[bar]]></item><item type="str"><![CDATA[baz]]>' \
                      b'</item></mylist><mydict type="dict"><foo type="str"><![CDATA[bar]]></foo><baz type="int">' \
                      b'<![CDATA[1]]></baz></mydict><ok type="bool"><![CDATA[True]]>' \
                      b'</ok></root>'

    assert dicttoxml(payload, cdata=True) == expected


def test_without_cdata() -> None:
    payload: dict = {'mylist': ['foo', 'bar', 'baz'], 'mydict': {'foo': 'bar', 'baz': 1}, 'ok': True}
    expected: bytes = b'<?xml version="1.0" encoding="UTF-8" ?><root><mylist type="list"><item type="str">foo</item>' \
                      b'<item type="str">bar</item><item type="str">baz</item></mylist><mydict type="dict">' \
                      b'<foo type="str">bar</foo><baz type="int">1</baz></mydict><ok type="bool">True</ok></root>'

    assert dicttoxml(payload) == expected


def test_custom_item_name() -> None:
    payload: dict = {'mylist': ['foo', 'bar', 'baz'], 'mydict': {'foo': 'bar', 'baz': 1}, 'ok': True}

    expected: bytes = b'<?xml version="1.0" encoding="UTF-8" ?><root><mylist type="list"><list_item type="str">foo' \
                      b'</list_item><list_item type="str">bar</list_item><list_item type="str">baz</list_item>' \
                      b'</mylist><mydict type="dict"><foo type="str">bar</foo><baz type="int">1</baz></mydict>' \
                      b'<ok type="bool">True</ok></root>'

    assert dicttoxml(payload, item_func=lambda x: 'list_item') == expected


def test_accept_basic_iterator() -> None:
    myiterator = range(1, 11)
    expected: bytes = b'<?xml version="1.0" encoding="UTF-8" ?><root><item type="int">1</item><item type="int">2' \
                      b'</item><item type="int">3</item><item type="int">4</item><item type="int">5</item>' \
                      b'<item type="int">6</item><item type="int">7</item><item type="int">8</item>' \
                      b'<item type="int">9</item><item type="int">10</item></root>'

    assert dicttoxml(myiterator) == expected


def test_unique_id_feature() -> None:
    payload: dict = {'mylist': ['foo', 'bar', 'baz'], 'mydict': {'foo': 'bar', 'baz': 1}, 'ok': True}

    assert dicttoxml(payload, ids=True).count(b'id=') == 8


def test_disable_root() -> None:
    payload: dict = {'mylist': ['foo', 'bar', 'baz'], 'mydict': {'foo': 'bar', 'baz': 1}, 'ok': True}
    expected: bytes = b'<mylist type="list"><item type="str">foo</item><item type="str">bar</item><item type="str">' \
                      b'baz</item></mylist><mydict type="dict"><foo type="str">bar</foo><baz type="int">1</baz>' \
                      b'</mydict><ok type="bool">True</ok>'

    assert dicttoxml(payload, root=False) == expected


def test_primitive_bool_convert() -> None:
    data = OrderedDict()

    data['true'] = True
    data['false'] = False
    data['int'] = 42
    data['float'] = 42.0
    data['None'] = None
    data['string'] = 'str_value'

    assert dicttoxml(data, root=False, attr_type=False) == b"<true>True</true><false>False</false><int>42</int><float>42.0</float><None></None><string>str_value</string>"


def test_folding_list_ignored() -> None:
    payload: dict = {'book': [{'title': 'Python Programming', 'license': 'GPL', 'author': ['Adam', 'Benny', 'Charlie']}, {'license': 'Apache 2.0', 'title': 'Business Modelling'}]}

    assert dicttoxml(payload, fold_list=False, attr_type=False) == b'<?xml version="1.0" encoding="UTF-8" ?><root><book><title>Python Programming</title><license>GPL</license><author>Adam</author><author>Benny</author><author>Charlie</author></book><book><license>Apache 2.0</license><title>Business Modelling</title></book></root>'


def test_fix_dict_integer_key() -> None:
    payload: dict = {1: "abc"}

    assert dicttoxml(payload) == b'<?xml version="1.0" encoding="UTF-8" ?><root><n1 type="str">abc</n1></root>'
