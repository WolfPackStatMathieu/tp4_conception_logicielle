from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from application.model.calculette import Calculette
from application.model.interpreteur_wrapper import InterpreteurWrapper


# Mappé a / dans le fichier urls.py
@csrf_exempt
def home(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        a = request.POST.get("first")
        op = request.POST.get("operation")
        b = request.POST.get("second")
        a = int(a)
        b = int(b)
        calculette = Calculette()
        z = 0
        if op == "+":
            z = calculette.somme(a, b)
        elif op == "-":
            z = calculette.soustraction(a, b)
        elif op == "*":
            z = calculette.produit(a, b)
        elif op == "/":
            z = calculette.division(a, b)

        return render(request, "application/result.html", context={"z": z})

    return render(request, "application/home.html")


def calculer_from_expression(expression: str):
    return InterpreteurWrapper().calculer_from_expression(expression=expression)


# Mappé a /string dans le fichier urls.py
@csrf_exempt
def string(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        expression = request.POST.get("expression")
        z = calculer_from_expression(expression)
        return render(request, "application/result.html", context={"z": z})
    return render(request, "application/string.html")
