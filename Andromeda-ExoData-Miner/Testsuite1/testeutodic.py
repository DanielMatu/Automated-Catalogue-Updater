from DataRetrival import eutodic
import unittest

class TestEutodic(unittest.TestCase):
    '''Test all functions of  eutodic.py
    '''
    def setUp(self):
        self._eu_dict = eutodic.build_dict()

    def testisEuDict(self):
        self.assertEqual('detection_type' in self._eu_dict.keys(), True)