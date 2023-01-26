from application.model.interpreteur import Interpreteur
from application.model.interpreteur_impl.no_parentheses_interpreteur import (
    NoParenthesesInterpreteur,
)
from application.model.interpreteur_impl.parentheses_interpreteur import (
    ParenthesesInterpreteur,
)


class InterpreteurWrapper:
    def __init__(self):
        self.interpreteur: Interpreteur = ParenthesesInterpreteur()
        if True:
            self.interpreteur: Interpreteur = NoParenthesesInterpreteur()

    def calculer_from_expression(self, expression: str):
        return self.interpreteur.calculer_from_expression(expression=expression)
