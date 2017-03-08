from DataRetrival import nasatodic
import unittest


class TestNasatodic(unittest.TestCase):
    '''Test all functions of  nasatodic.py
    '''

    def setUp(self):
        self._nasa_dict = nasatodic.crawler()

    def testisNasaDict(self):
        self.assertEqual('pl_discmethod' in self._nasa_dict.keys(), True)
