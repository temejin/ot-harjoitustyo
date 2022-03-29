import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.1")

    def test_saldo_vahenee_oikein_jos_tarpeeksi_rahaa(self):
        nosto = self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
        self.assertEqual(True, nosto)

    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        nosto = self.maksukortti.ota_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        self.assertEqual(False, nosto)
