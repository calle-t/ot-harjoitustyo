# tehtävä 8

import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self) -> None:
        self.kassapaate = Kassapaate()
        self.pienikortti = Maksukortti(100)
        self.suurikortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_rahamäärä_ja_myytyjen_lounaiden_määrä_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_toimii_edullisten_lounaiden_osalta(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(1000), 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_toimii_maukkaiden_lounaiden_osalta(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1000), 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_korttiosto_toimii_edullisten_lounaiden_osalta(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.pienikortti), False)
        self.assertEqual(self.pienikortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.suurikortti), True)
        self.assertEqual(self.suurikortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_maukkaiden_lounaiden_osalta(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.pienikortti), False)
        self.assertEqual(self.pienikortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.suurikortti), True)
        self.assertEqual(self.suurikortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_rahamaara_kasvaa(self):
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.pienikortti,-100),None)

        self.kassapaate.lataa_rahaa_kortille(self.pienikortti, 900)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100900)
        self.assertEqual(self.pienikortti.saldo, 1000)