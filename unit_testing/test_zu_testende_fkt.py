import unittest

from zu_testende_funk import ist_gerade



class TestGeradeFkt(unittest.TestCase):

    def test_ist_gerade(self):
        assert ist_gerade(4) is False


if __name__ == '__main__':
    unittest.main()

"""
    Was sind meine Testfälle ?



print(ist_gerade(4)) # True
print(ist_gerade(3)) # False
print(ist_gerade(0)) # True
"""