from DataRetrival import xmldictonary
import unittest

class TestXmldictonary(unittest.TestCase):
    '''Test all functions of  xmldictonary.py
    '''

    def setUp(self):
        self._convdict = xmldictonary.orgxmlconvert
        self._originaldict = xmldictonary.orgxmldict

    def testkeysExistOrg(self):
        self.assertEqual(len(self._originaldict.key()), 164)

    def testkeysExistConv(self):
        self.assertEqual(len( self._convdict.key()), 164)