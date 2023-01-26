import unittest

from application.model.interpreteur_impl.no_parentheses_interpreteur import (
    NoParenthesesInterpreteur,
)


class InterpreteurTest(unittest.TestCase):
    def test_no_parentheses_interpreter_calculer_from_expression_raise_character_invalid(
        self,
    ):
        """
        On suppose que lorsque l'utilisateur met des caractères incohérent, l'on jette une exception
        """
        no_parenthese_interpreter = NoParenthesesInterpreteur()
        self.assertRaises(
            ValueError,
            lambda: no_parenthese_interpreter.calculer_from_expression("a + b + c"),
        )

    def test_no_parentheses_interpreter_calculer_from_expression_raise_order_invalid(
        self,
    ):
        """
        On suppose que lorsque l'utilisateur ordonne mal les symboles, l'on jette une exception
        """
        no_parenthese_interpreter = NoParenthesesInterpreteur()
        self.assertRaises(
            ValueError,
            lambda: no_parenthese_interpreter.calculer_from_expression("1 + + 2 + 3"),
        )

    def test_no_parentheses_interpreter_calculer_from_expression(self):
        """
        On suppose que lorsque l'utilisateur met 1+2+3, l'on obtient 6
        """
        pass

    def test_no_parentheses_interpreter_calculer_from_expression_correctly_strip(self):
        """
        On suppose que lorsque l'utilisateur met 1 + 2 + 3, l'on obtient 6
        ( et donc avec le test plus haut que les espaces ne gênent pas)
        """
        no_parenthese_interpreter = NoParenthesesInterpreteur()
        actual = no_parenthese_interpreter.calculer_from_expression("1 + 2 + 3")
        self.assertEqual(6, actual)


if __name__ == "__main__":
    unittest.main()
