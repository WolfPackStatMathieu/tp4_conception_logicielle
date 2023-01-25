from application.model.calculette import Calculette
from application.model.interpreteur_impl import Interpreteur
from application.model.interpreteur_impl.parentheses_interpreteur import (
    ParenthesesInterpreteur,
)


class InterpreteurWrapper:
    def __init__(self):
        self.interpreteur: Interpreteur = ParenthesesInterpreteur()

    def calculer_from_expression(self, expression: str):
        return self.interpreteur.calculer_from_expression(expression=expression)
