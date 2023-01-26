from application.model.calculette import Calculette
from application.model.interpreteur import Interpreteur


class NoParenthesesInterpreteur(Interpreteur):
    def calculer_from_expression(self, expression: str):
        without_spaces_expression = expression.replace(" ", "")
        if self._invalid_characters(expression=without_spaces_expression):
            raise ValueError("invalid characters found in expression")
        if self._invalid_syntax(expression=without_spaces_expression):
            raise ValueError("invalid ordering of values in expression")
        calculette = Calculette()
        calcul = calculette.compute(without_spaces_expression)
        return calcul

    def _invalid_characters(self, expression: str):
        import re

        regex = "[0-9| |+|-|*|\/]"
        res = re.findall(regex, expression)
        return len(res) != len(expression)

    def _invalid_syntax(self, expression: str):
        import re

        regex = "[0-9][+|-|*|\/]"
        res = re.findall(regex, expression.replace(" ", ""))
        nb_caracteres_matches = len("".join(res))
        return (nb_caracteres_matches + 1) != len(expression.replace(" ", ""))
