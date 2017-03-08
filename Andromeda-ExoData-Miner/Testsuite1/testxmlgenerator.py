from UserInteractionBackend_python import xmlgenerator
import unittest
import os


class TestXmlgenerator(unittest.TestCase):
    '''Test all functions of  xmlgenerator.py
    '''

    def setUp(self):
        xmlgenerator.xmlgenerator(7, "systems_eu", 0)

    def testFileCreationNasa(self):
        try:
            os.rmdir("../UserInteractionBackend_python/systems_nasa")
            directoryempty = True
        except OSError:
            directoryempty = False

        self.assertEqual(directoryempty, True)

    def testFileCreationEu(self):
        try:
            os.rmdir("../UserInteractionBackend_python/systems_eu")
            directoryempty = True
        except OSError:
            directoryempty = False

        self.assertEqual(directoryempty, True)

    def testXMLMadeNasa(self):
        self.assertEqual((os.listdir("../UserInteractionBackend_python/systems_nasa")[0]).endswith('.xml'), True)

    def testXMLMadeEu(self):
        self.assertEqual((os.listdir("../UserInteractionBackend_python/systems_eu")[0]).endswith('.xml'), True)
