class Calculette:
    def somme(self, a: int, b: int):
        return a + b

    def soustraction(self, a: int, b: int):
        return a - b

    def produit(self, a: int, b: int):
        return a * b

    def division(self, numerateur: int, denominateur: int):
        if denominateur == 0:
            return "Erreur, division par zéro"
        return numerateur / denominateur

    def compute(self, expression: str):
        return eval(expression)
