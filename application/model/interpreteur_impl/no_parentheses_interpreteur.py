from application.model.calculette import Calculette
from application.model.interpreteur import Interpreteur


class NoParenthesesInterpreteur(Interpreteur):
    def calculer_from_expression(self, expression: str):
        without_spaces_expression = expression.replace(" ", "")
        if self._contains_invalid_characters(expression=without_spaces_expression):
            raise ValueError("invalid characters found in expression")
        if self._has_invalid_syntax(expression=without_spaces_expression):
            raise ValueError("invalid ordering of values in expression")
        calcul = self.compute(self, expression)
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

    def compute(self, expression: str) -> int:
        if "*" in expression or "/" in expression:
            index = expression.index("*")
            operation = self.__effectuer_operation(
                expression[index - 1], expression[index], expression[index + 1]
            )
            new_expression = (
                expression[: index - 1 :] + operation + expression[index + 1 : :]
            )
            self.compute(new_expression)
        operation = self.__effectuer_operation(
            expression[0], expression[1], expression[2]
        )
        new_expression = operation + expression[index + 1 : :]
        try:
            self.compute(new_expression)
        except:
            return int(expression)

    def __effectuer_operation(self, number1: str, operator: str, number2: str):
        function = self.get_function(operator)
        result = function(number1, number2)
        return str(result)

    def get_function(self, char: str) -> callable:
        if char == "+":
            return lambda a, b: Calculette.somme(a, b)
        if char == "-":
            return lambda a, b: Calculette.soustraction(a, b)
        if char == "*":
            return lambda a, b: Calculette.produit(a, b)
        if char == "/":
            return lambda a, b: Calculette.division(a, b)
        else:
            raise NotImplementedError("operator not implemented")
