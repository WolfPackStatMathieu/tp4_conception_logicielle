from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method == "POST":
        a = request.POST.get("first")
        op = request.POST.get("operation")
        # print(op)
        b = request.POST.get("second")
        a = int(a)
        b = int(b)
        # print("{} {}".format(a, b))
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

        return render(request, "calculate/result.html", context={"z": z})

    return render(request, "calculate/home.html")


def string(request):
    return render(request, "calculate/string.html")
