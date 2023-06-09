import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    # omat testit, tehtävä 6

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_rahan_ottaminen(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, 900)

        self.maksukortti.ota_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo, 900)

        self.assertEqual(self.maksukortti.ota_rahaa(1000), False)
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)