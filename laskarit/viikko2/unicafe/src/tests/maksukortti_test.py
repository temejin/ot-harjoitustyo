import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alustuu_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataus_lataa_oikean_maaran(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_rahaa_ottaessa_saldo_vahenee_oikein_mikali_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_rahaa_ottaessa_rahaa_saldo_ei_vahene_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(3000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_otto_palauttaa_true_jos_rahaa_on_tarpeeksi(self):
        vastaus = self.maksukortti.ota_rahaa(500)
        self.assertEqual(vastaus, True)

    def test_rahan_otto_palauttaa_false_jos_rahaa_ei_ole_tarpeeksi(self):
        vastaus = self.maksukortti.ota_rahaa(5000)
        self.assertEqual(vastaus, False)
        
    def test_maksukortin_merkkijonoesitys_on_oikeanlainen(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
