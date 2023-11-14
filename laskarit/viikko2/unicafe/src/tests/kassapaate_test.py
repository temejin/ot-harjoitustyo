import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaate_alustuu_oikein(self):
        myydyt_lounaat = self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(myydyt_lounaat, 0)

    def test_syo_edullisesti_kateisella_riittava_maksu_kasvattaa_kassan_rahaa_ja_antaa_vaihtorahan(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(vaihtoraha, 260)

    def test_syo_edullisesti_kateisella_riittava_maksu_kasvattaa_syotyjen_edullisten_lounaiden_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_syo_edullisesti_kateisella_vajaa_maksu_palauttaa_maksun_eika_muuta_kassaa(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(vaihtoraha, 200)

    def test_syo_maukkaasti_kateisella_riittava_maksu_kasvattaa_kassan_rahaa_ja_antaa_vaihtorahan(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(vaihtoraha, 100)

    def test_syo_maukkaasti_kateisella_riittava_maksu_kasvattaa_syotyjen_maukkaiden_lounaiden_maaraa(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_vajaa_maksu_palauttaa_maksun_eika_muuta_kassaa(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(vaihtoraha, 300)

    def test_syo_edullisesti_kortilla_riittavalla_saldolla_veloittaa_summan_ja_palauttaa_true(self):
        tulos = self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(tulos, True)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.60)

    def test_syo_edullisesti_kortilla_riittavalla_saldolla_kasvattaa_syotyjen_lounaiden_maaraa(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_syo_edullisesti_kortilla_vajaalla_saldolla_ei_veloita_kortilta_eika_kasvata_myytyjen_lounaiden_maaraa(self):
        kortti = Maksukortti(200)
        tulos = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 2.0)
        self.assertEqual(self.kassa.edulliset,0)
        self.assertEqual(tulos, False)

    def test_syo_maukkaasti_kortilla_riittavalla_saldolla_veloittaa_summan_ja_palauttaa_true(self):
        tulos = self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(tulos, True)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)

    def test_syo_maukkaasti_kortilla_riittavalla_saldolla_kasvattaa_suotyjen_maukkaiden_lounaiden_maaraa(self):
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_vajaalla_saldolla_ei_veloita_kortilta_eika_kasvata_myytyjen_lounaiden_maaraa(self):
        kortti = Maksukortti(200)
        tulos = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 2.0)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(tulos, False)

    def test_korttimaksu_ei_muuta_kassan_rahamaaraa(self):
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortille_rahan_lataaminen_muuttaa_kortin_saldoa_ja_lisaa_rahan_kassaan(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1010.0)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_negatiivisen_summan_lataus_kortille_ei_tee_mitaan(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
