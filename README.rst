=======================
Testing XML with Python
=======================

This library is a set of helper methods for testing XML in Python.

Sample usage
------------

To use these additional assertions, simply mix the ``xmltest.XMLAssertions`` class
into your test case::

    import unittest
    from xmltest import XMLAssertions

    class MyTestCase(unittest.TestCase, XMLAssertions):
        pass

Assert the value of a particular element::

    self.assertXMLElementText(xml, 'hello', 'Response.message')

Assert the attribute values of an element::

    self.assertXMLElementAttributes(xml, {'a': 'something'}, 'Response.message'}

Installation
------------

From PyPi::

    pip install unittest-xml

Contributing
------------

To run the tests, install ``nose`` and ``mock``::

    pip install nose mock

and use::

    nosetests

to run the tests.