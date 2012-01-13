=========================
Testing XML with unittest
=========================

This library is a set of helper methods for testing XML with Python's unittest library.
The new assertion methods use `XPath`_ to select the XML elements that assertions are being
made about.

.. _`XPath`: http://en.wikipedia.org/wiki/XPath

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

Assert the number of elements matching an XPath query::

    self.assertXPathNodeCount(response_xml, 1, 'CardTxn/issuer[@country="UK"]')
    self.assertXPathNodeCount(response_xml, 1, 'status')

Assert the value of a particular element::

    self.assertXPathNodeText(response_xml, 'ACCEPTED', 'reason')

Assert the attribute values of an element::

    self.assertXPathNodeAttributes(xml, {'country': 'UK'}, 'CardTxn/issuer'}

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