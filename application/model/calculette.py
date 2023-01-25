class Calculette:
    @staticmethod
    def somme(a: int, b: int):
        a = a + b
        return a

    @staticmethod
    def soustraction(a: int, b: int):
        return a - b

    @staticmethod
    def produit(a: int, b: int):
        return a * b

    @staticmethod
    def division(numerateur: int, denominateur: int):
        if denominateur == 0:
            return "Error! Division by zero isn't possible"
        return numerateur / denominateur
