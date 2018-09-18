import unittest
import check_uniq_symbol

class TestUniqSymbol(unittest.TestCase):
    def test_not_uniq_string(self):
        self.assertFalse(check_uniq_symbol.check_uniq_symbols('qq'))

    def test_uniq_string(self):
        self.assertTrue(check_uniq_symbol.check_uniq_symbols('qWertY'))

if __name__ == '__main__':
    unittest.main()
