class Calculette:
    def somme(self, a: int, b: int):
        return a + b

    def soustraction(self, a: int, b: int):
        """effectue la soustraction a - b

        Args:
            a (int): nombre de départ auquel on va soustraire b
            b (int): nombre qu'on soustrait

        Returns:
            int: résultat de a - b 
        """
        return a - b

    def produit(self, a: int, b: int):
        return a * b

    def division(self, numerateur: int, denominateur: int):
        if denominateur == 0:
            return "Erreur, division par zéro"
        return numerateur / denominateur

    def compute(self, expression: str):
        return eval(expression)
