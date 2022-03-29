import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_luonti_toimii_oikein(self):
        self.assertEqual(100000, self.kassa.kassassa_rahaa)
        self.assertEqual(0, self.kassa.edulliset)
        self.assertEqual(0, self.kassa.maukkaat)

    def test_riittava_edullinen_kateisosto(self):
        vaihtorahat = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(60, vaihtorahat)
        self.assertEqual(1, self.kassa.edulliset)
        self.assertEqual(100240, self.kassa.kassassa_rahaa)

    def test_riittava_maukas_kateisosto(self):
        vaihtorahat = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(100, vaihtorahat)
        self.assertEqual(1, self.kassa.maukkaat)
        self.assertEqual(100400, self.kassa.kassassa_rahaa)

    def test_riittamaton_edullinen_ostoyritys(self):
        vaihtorahat = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(200,vaihtorahat)
        self.assertEqual(0, self.kassa.edulliset)
        self.assertEqual(100000, self.kassa.kassassa_rahaa)

    def test_riittamaton_maukas_ostoyritys(self):
        vaihtorahat = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(300, vaihtorahat)
        self.assertEqual(0, self.kassa.maukkaat)
        self.assertEqual(100000, self.kassa.kassassa_rahaa)

    def test_edullinen_riittava_saldo(self):
        onnistuiko = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 7.6")
        self.assertEqual(True, onnistuiko)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_edullinen_riittamaton_saldo(self):
        onnistuiko = self.kassa.syo_edullisesti_kortilla(self.kortti)
        onnistuiko = self.kassa.syo_edullisesti_kortilla(self.kortti)
        onnistuiko = self.kassa.syo_edullisesti_kortilla(self.kortti)
        onnistuiko = self.kassa.syo_edullisesti_kortilla(self.kortti)
        onnistuiko = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 0.4")
        self.assertEqual(False, onnistuiko)
        self.assertEqual(self.kassa.edulliset, 4)

    def test_maukas_riittava_saldo(self):
        onnistuiko = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 6.0")
        self.assertEqual(True, onnistuiko)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maukas_riittamaton_saldo(self):
        onnistuiko = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        onnistuiko = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        onnistuiko = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 2.0")
        self.assertEqual(False, onnistuiko)
        self.assertEqual(self.kassa.maukkaat, 2)

    def test_lataa_rahaa_kortille_kelpo_summa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 2000)
        self.assertEqual(str(self.kortti), "saldo: 30.0")
        self.assertEqual(self.kassa.kassassa_rahaa,102000)

    def test_lataa_rahaa_kortille_negatiivinen_summa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(str(self.kortti), "saldo: 10.0")
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
