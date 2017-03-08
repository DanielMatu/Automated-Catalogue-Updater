from UserInteractionBackend_python import CompareIt, Driver
import unittest

class TestCompareIt(unittest.TestCase):
    '''Test all functions of  CompareIt.py
    '''
    def setUp(self):
        self._eu_dict = Driver.buildEUdict()
        CompareIt.OECify(self._eu_dict)
        self._nasa_dict = Driver.buildNasadict()
        CompareIt.OECify(self._nasa_dict)

    def testOECifyEU(self):
        self.assertEqual("<planet><discoverymethod>" in self._eu_dict.keys(), True)

    def testOECifyNasa(self):
        self.assertEqual("<planet><discoverymethod>" in self._nasa_dict.keys(), True)

    def testOecxmltags(self):
        self.assertEqual(CompareIt.oecxmltags('detection_type'), "<planet><discoverymethod>")




