from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "index.html", {"name": "Suraj"})


def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])

    res = val1 + val2

    return render(request, "result.html", {"sum": res})
