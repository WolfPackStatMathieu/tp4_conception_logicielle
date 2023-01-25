from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


# Mappé a / dans le fichier urls.py
def home(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        a = request.POST.get("first")
        op = request.POST.get("operation")
        b = request.POST.get("second")
        a = int(a)
        b = int(b)
        z = 0
        if op == "+":
            z = a + b
        elif op == "-":
            z = a - b
        elif op == "*":
            z = a * b
        elif op == "/":
            if b == 0:
                z = "Error! Division by zero isn't possible"
            else:
                z = a / b

        return render(request, "application/result.html", context={"z": z})

    return render(request, "application/home.html")


def calculer_from_expression(expression: str):
    return 2


# Mappé a /string dans le fichier urls.py
def string(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        expression = request.POST.get("expression")
        z = calculer_from_expression(expression)
        return render(request, "application/result.html", context={"z": z})
    return render(request, "application/string.html")
