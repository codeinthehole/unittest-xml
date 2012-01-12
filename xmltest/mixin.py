from xml.dom.minidom import parseString
from xml.parsers.expat import ExpatError


class XMLAssertions(object):

    def _extract_element(self, xml_str, element_path):
        try:
            doc = parseString(xml_str)
        except ExpatError:
            raise self.failureException("Invalid XML")
        elements = element_path.split('.')
        parent = doc
        for element_name in elements:
            sub_elements = parent.getElementsByTagName(element_name)
            if len(sub_elements) == 0:
                msg = "No element matching '%s' found using XML string '%s'" % (element_name, element_path)
                raise self.failureException(msg)
            parent = sub_elements[0]
        return parent

    def assertXMLElementText(self, xml_str, value, element_path):
        """
        Assert that an XML string contains an element
        with value matching that passed.
        """
        element = self._extract_element(xml_str, element_path)
        self.assertEqual(value, element.firstChild.data)

    def assertXMLElementAttributes(self, xml_str, attributes, element_path):
        """
        Assert that an XML element contains a given set of attributes
        """
        element = self._extract_element(xml_str, element_path)
        for attribute, value in attributes.items():
            self.assertEqual(value, element.attributes[attribute].value)
         