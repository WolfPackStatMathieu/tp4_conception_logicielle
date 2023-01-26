import unittest

from application.model.calculette import Calculette


class CalculetteTest(unittest.TestCase):
    def test_somme(self):
        expected = 2
        actual = Calculette().somme(1, 1)
        self.assertEqual(expected, actual)

    def test_division(self):
        expected = 2
        actual = Calculette().division(2, 1)
        self.assertEqual(expected, actual)

    def test_division_float(self):
        expected = 1.5
        actual = Calculette().division(3, 2)
        self.assertEqual(expected, actual)

    def test_produit(self):
        expected = 2
        actual = Calculette().produit(1, 2)
        self.assertEqual(expected, actual)

    @unittest.skip("not yet implemented")
    def test_division_should_throw_exception_on_division_by_0(self):
        self.assertRaises(ValueError, Calculette().division(2, 0))


if __name__ == "__main__":
    unittest.main()
