import unittest
from  unit_testing.aufgabe import versandkosten

"""Aufgabe:
Schreibe für Versandkosten Testfälle achte auf Grenzfälle"""

class TestVersandkosten(unittest.TestCase):
    
    def test_versandkosten_fuer_negative(self):
        with self.assertRaises(ValueError):
            versandkosten(-2)

    def test_schwerste_pakete(self):
        self.assertEqual(versandkosten(10), 7.99)

    def test_kleine_pakete(self):
        self.assertEqual(versandkosten(0.9), 2.99)

    def test_kleine_pakete_grenze(self):
        self.assertEqual(versandkosten(1), 4.99)
    
    def test_mittlere_pakete_grenze(self):
        self.assertEqual(versandkosten(4.9), 4.99)

    def test_mittlere_pakete_grenze(self):
        self.assertEqual(versandkosten(5), 7.99)

if __name__ == '__main__':
    unittest.main()