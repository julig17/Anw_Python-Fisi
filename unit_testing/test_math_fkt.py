"""Unit Tests für die mathematischen Funktionen in math_fkt.py"""
# Die Unit Tests überprüfen die Korrektheit der Funktionen, 
# indem sie verschiedene Eingabewerte testen und die erwarteten 
# Ergebnisse mit den tatsächlichen Ergebnissen vergleichen.
#zunächst wird die unittest Bibliothek importiert, um die Unit Tests zu erstellen
#und die Funktionen aus dem Modulmath_fkt.py importiert, 
# damit sie in den Tests verwendet werden
import unittest
from unit_testing.math_fkt import sum, minus, mal, durch, sum_zwei


#Um nun einen Test zu implementieren, brauchen wir eine Testklasse.
# Typisch beginnt der Name mit Test und erbte von unittest.TestCase
#jede Methode aus dem MathFkt Modul wird in einer eigenen Testmethode getestet,
# die mit test_ beginnt, damit unittest sie als Testmethode erkennt.
class TestMathFkt(unittest.TestCase):
    def test_sum_zwei(self):
        #Die assertEqual Methode wird verwendet, 
        # um zu überprüfen, ob das Ergebnis der Funktion sum_zwei 
        # mit dem erwarteten Wert übereinstimmt.
        self.assertEqual(sum_zwei(2, 3), 5)
        self.assertEqual(sum_zwei(-1, 1), 0)
        # Prüft ob der Error aufgetreten ist beim Abruf der Funktion
        # mit den gegebenden Argumenten
        with self.assertRaises(TypeError):
            sum_zwei(2, '3')

    def test_minus(self):
        self.assertEqual(minus(5, 2), 3)
        self.assertEqual(minus(0, 4), -4)
        with self.assertRaises(TypeError):
            minus(2, '3')

    def test_mal(self):
        self.assertEqual(mal(3, 4), 12)
        self.assertEqual(mal(-2, 5), -10)
        with self.assertRaises(TypeError):
            mal(2, '3')

    def test_durch(self):
        self.assertEqual(durch(10, 2), 5)
        self.assertEqual(durch(7, -1), -7)
        with self.assertRaises(ValueError):
            durch(5, 0)
        with self.assertRaises(TypeError):
            durch(2, '3')

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6)
        self.assertEqual(sum([]), 0)
        with self.assertRaises(TypeError):
            sum([1, '2', 3])    

if __name__ == '__main__':
    unittest.main()