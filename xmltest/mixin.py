from xml.dom.minidom import parseString
from xml.parsers.expat import ExpatError
from xml.etree import ElementTree


class XMLAssertions(object):

    def assertXPathNodeCount(self, xml_str, num, xpath):
        doc = ElementTree.fromstring(xml_str)
        self.assertEqual(num, len(doc.findall(xpath)))

    def assertXPathNodeText(self, xml_str, expected, xpath):
        doc = ElementTree.fromstring(xml_str)
        self.assertEqual(expected, doc.findtext(xpath))

    def assertXPathNodeAttributes(self, xml_str, attributes, xpath):
        doc = ElementTree.fromstring(xml_str)
        ele = doc.find(xpath)
        for attribute, value in attributes.items():
            self.assertTrue(attribute in ele.attrib)
            self.assertEqual(value, ele.attrib[attribute])





         