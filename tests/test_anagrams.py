import unittest

from anagrams import *

class TestAnagrams(unittest.TestCase):
    def setUp(self):
        self.a = Anagrams()

    def test_abba_baab(self):
        self.assertEqual( self.a.anagrams('abba', ['baab']), ['baab'])

    def test_abba(self):
        self.assertEqual( self.a.anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'] )

    def test_racer(self):
        self.assertEqual( self.a.anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'] )

    def test_laser(self):
        self.assertEqual( self.a.anagrams('laser', ['lazing', 'lazy',  'lacer']), [] )


if __name__ == "__main__":
    unittest.main()

