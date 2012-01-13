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


class XMLMixinTests(unittest.TestCase):

    def setUp(self):
        self.test = type('SampleTestCase', 
                (unittest.TestCase, XMLAssertions), 
                {'runTest': lambda x: x})()
        self.test.assertEqual = Mock()
        self.test.assertTrue = Mock()

    def test_asserting_number_of_elements(self):
        self.test.assertXPathNodeCount(SAMPLE_XML, 1, './/reason')
        self.test.assertEqual.assert_called_once_with(1, 1)

    def test_asserting_node_text(self):
        self.test.assertXPathNodeText(SAMPLE_XML, 'ACCEPTED', 'reason')
        self.test.assertEqual.assert_called_once_with('ACCEPTED', 'ACCEPTED')

    def test_asserting_node_text_using_attribute_query(self):
        self.test.assertXPathNodeText(SAMPLE_XML, 'LIVE', 'mode[@type="sample"]')
        self.test.assertEqual.assert_called_once_with('LIVE', 'LIVE')

    def test_asserting_node_text_for_invalid_query(self):
        self.test.assertXPathNodeText(SAMPLE_XML, 'ACCEPTED', 'badelement')
        self.test.assertEqual.assert_called_once_with('ACCEPTED', None)

    def test_asserting_attribute_values(self):
        self.test.assertXPathNodeAttributes(SAMPLE_XML, {'type': 'sample'}, 'mode') 
        self.test.assertEqual.assert_called_once_with('sample', 'sample')
        self.test.assertTrue.assert_called_once_with(True)
