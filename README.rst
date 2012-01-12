=========================
Testing XML with unittest
=========================

This library is a set of helper methods for testing XML with Python's unittest library

Sample usage
------------

To use these additional assertions, simply mix the ``xmltest.XMLAssertions`` class
into your test class::

    import unittest
    from xmltest import XMLAssertions

    class MyTestCase(unittest.TestCase, XMLAssertions):
        pass

Now suppose you have the following XML string that you wish to examine::

    response_xml = """<?xml version="1.0" encoding="UTF-8" ?>
    <Response>
        <CardTxn>
            <authcode>060642</authcode>
            <card_scheme>Switch</card_scheme>
            <issuer country="UK">HSBC</issuer>
        </CardTxn>
        <reference>3000000088888888</reference>
        <merchantreference>1000001</merchantreference>
        <mode>LIVE</mode>
        <reason>ACCEPTED</reason>
        <status>1</status>
        <time>1071567305</time>
    </Response>"""

Assert the value of a particular element::

    self.assertXMLElementText(response_xml, 'ACCEPTED', 'Response.reason')

Assert the attribute values of an element::

    self.assertXMLElementAttributes(xml, {'country': 'UK'}, 'Response.CardTxn.issuer'}

As you can see, the assertion methods use a simple dot-separated syntax for referencing
XML elements - not very sophisticated but sufficient for many situations.  Fancy
XPath-driven assertions to come later.

Installation
------------

From PyPi (coming soon)::

    pip install unittest-xml

Contributing
------------

To run the tests, install ``nose`` and ``mock``::

    pip install nose mock

and use::

    nosetests

to run the tests.