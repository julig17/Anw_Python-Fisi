import unittest
from  unit_testing.aufgabe import maximum_von_zwei_zahlen

"""Aufgabe:
Schreibe für diese Testfälle UnitTests
print(maximum_von_zwei_zahlen("3",10))
print(maximum_von_zwei_zahlen(10,5))
print(maximum_von_zwei_zahlen(10,10))
print(maximum_von_zwei_zahlen(7,-7))"""

class TestMaximum(unittest.TestCase):
    def test_maximum_von_zwei_integer(self):
            self.assertEqual(maximum_von_zwei_zahlen(2, 3), 3)

    def test_maximum_von_zwei_wirft_fehler_wenn_ein_parameter_kein_int(self):
            with self.assertRaises(TypeError):
                maximum_von_zwei_zahlen(2, '3')

    def test_maximum_von_gleichen_zahlen(self):
            self.assertEqual(maximum_von_zwei_zahlen(2, 2), 2)

    def test_maximum_von_negativen_zahlen(self):
            self.assertEqual(maximum_von_zwei_zahlen(2, -2), 2)

            
if __name__ == '__main__':
    unittest.main()