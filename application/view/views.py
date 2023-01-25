from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from application.model.calculette import Calculette
from application.model.interpreteur_wrapper import Interpreteur


# Mappé a / dans le fichier urls.py
@csrf_exempt
def home(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        a = request.POST.get("first")
        op = request.POST.get("operation")
        b = request.POST.get("second")
        a = int(a)
        b = int(b)
        z = 0
        if op == "+":
            z = Calculette.somme(a, b)
        elif op == "-":
            z = Calculette.soustraction(a, b)
        elif op == "*":
            z = Calculette.produit(a, b)
        elif op == "/":
            z = Calculette.division(a, b)

        return render(request, "application/result.html", context={"z": z})

    return render(request, "application/home.html")


def calculer_from_expression(expression: str):
    return 2


# Mappé a /string dans le fichier urls.py
@csrf_exempt
def string(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        expression = request.POST.get("expression")
        z = Interpreteur.calculer_from_expression(expression)
        return render(request, "application/result.html", context={"z": z})
    return render(request, "application/string.html")
