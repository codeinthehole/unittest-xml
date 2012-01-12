import unittest
from mock import Mock
from xmltest import XMLAssertions

SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8" ?>
<Response>
    <CardTxn>
        <authcode>060642</authcode>
        <card_scheme>Switch</card_scheme>
        <country>United Kingdom</country>
        <issuer>HSBC</issuer>
    </CardTxn>
    <datacash_reference>3000000088888888</datacash_reference>
    <merchantreference>1000001</merchantreference>
    <mode type="sample">LIVE</mode>
    <reason>ACCEPTED</reason>
    <status>1</status>
    <time>1071567305</time>
</Response>"""

INVALID_XML = """This isn't XML"""


class SampleTestCase(XMLAssertions):
    failureException = AssertionError


class XMLMixinTests(unittest.TestCase, XMLAssertions):

    def setUp(self):
        self.test = SampleTestCase()
        self.test.assertEqual = Mock()
        self.test.fail = Mock()

    def test_invalid_xml_raises_assertion(self):
        print "asdf", self.failureException
        with self.assertRaises(SampleTestCase.failureException):
            self.test.assertXMLElementText(INVALID_XML, 'ACCEPTED', 'Response.reason')

    def test_valid_element_text_comparison(self):
        self.test.assertXMLElementText(SAMPLE_XML, 'ACCEPTED', 'Response.reason')
        self.test.assertEqual.assert_called_once_with('ACCEPTED', 'ACCEPTED')

    def test_invalid_element_text_comparison(self):
        with self.assertRaises(SampleTestCase.failureException):
            self.test.assertXMLElementText(SAMPLE_XML, 'ACCEPTED', 'Response.badelement')

    def test_invalid_element_fail_message(self):
        try:
            self.test.assertXMLElementText(SAMPLE_XML, 'ACCEPTED', 'Response.badelement')
        except AssertionError, e:
            msg = str(e)
            self.assertTrue('No element matching' in msg)

    def test_attribute_comparison(self):
        self.test.assertXMLElementAttributes(SAMPLE_XML, {'type': 'sample'}, 'Response.mode') 
        self.test.assertEqual.assert_called_once_with('sample', 'sample')
