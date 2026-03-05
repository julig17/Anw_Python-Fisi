import unittest

from  unit_testing.zu_testende_funk import ist_gerade


class TestGeradeFkt(unittest.TestCase):

    #print(ist_gerade(4)) # True
    def test_ist_gerade(self):
        assert ist_gerade(4) is True

    #print (ist_gerade(3)) # False
    def test_ist_ungrade(self):
        assert ist_gerade(3) is False

    def test_ist_gerade_auch_große_zahlen(self):
        assert ist_gerade(10000) is True

    def test_null(self):
        assert ist_gerade(0) is True


if __name__ == '__main__':
    unittest.main()

