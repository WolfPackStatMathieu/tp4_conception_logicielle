from application.model.interpreteur import Interpreteur


class NoParenthesesInterpreteur(Interpreteur):
    def calculer_from_expression(self, expression: str):
        if self._contains_invalid_characters(expression=expression):
            raise ValueError("invalid characters found in expression")
        if self._has_invalid_syntax(expression=expression):
            raise ValueError("invalid ordering of values in expression")

        return calcul

    def _contains_invalid_characters(self, expression: str):
        import re

        regex = "[0-9| |+|-|*|\/]"
        res = re.findall(regex, expression)
        return len(res) != len(expression)

    def _has_invalid_syntax(self, expression: str):
        import re

        regex = "[0-9][+|-|*|\/]"
        res = re.findall(regex, expression.replace(" ", ""))
        nb_caracteres_matches = len("".join(res))
        return (nb_caracteres_matches + 1) != len(expression.replace(" ", ""))

    def compute(self, expression: str, temporary_result: int = 0) -> int:
        trimmed_expression = expression.replace(" ", "")
        while len(expression) > 0:
            computed_expression = trimmed_expression.slice(0, 1)

            compute()
        return temporary_result
