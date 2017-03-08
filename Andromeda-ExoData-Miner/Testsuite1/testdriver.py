from UserInteractionBackend_python import Driver
import unittest

class TestDriver(unittest.TestCase):
    '''Test all functions of  Driver.py
    '''
    def setUp(self):
        self._eu_dict = Driver.buildEUdict()
        self._nasa_dict = Driver.buildEUdict()

    def testisBuildEuDict(self):
        self.assertEqual('detection_type' in self._eu_dict.keys(), True)

    def testisBuildNasaDict(self):
        self.assertEqual('pl_discmethod' in self._nasa_dict.keys(), True)

