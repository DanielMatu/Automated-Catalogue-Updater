from UserInteractionBackend_python import MergeIt
from UserInteractionBackend_python import Driver
import unittest


class TestMergeIt(unittest.TestCase):
    '''Test functions of  MergeIt.py
    '''
    def setUp(self):
        self.eu = Driver.buildEUdict()
        self.nasa = Driver.buildNasadict()

    # check if the format changed such that keys are system names
    # since dictionaries aren't static, check for particular system we know

    def testOrganizeDicEU(self):
        self.eu = MergeIt.organizeDic(self.eu, 0)
        self.assertEqual(('YBP401' in list(self.eu)), True)
        self.nasa = MergeIt.organizeDic(self.nasa, 1)
        self.assertEqual(('HATS-12' in list(self.nasa)), True)

    # see if dict is unpacked
    def testUnpack(self):
        test = {"a":[1], "b":[1]}
        unpacked = MergeIt.unpack(test)
        self.assertEqual(unpacked,{0: 1, 1: 1})

    # check if the merge is complete
    # since dicts aren't stack, just check if keys are correct
    def testMergeSources(self):
        merged = MergeIt.mergeSources(self.eu, self.nasa)
        self.assertEqual(list(merged)[0], 0)
        self.assertEqual(list(merged)[5], 5)
