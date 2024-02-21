from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request,'blog/home.html',context)
   
def calculate(request):
    if request.method == 'POST':
        angka1 = request.POST.get("angka1")
        angka2 = request.POST.get("angka2")
        operation = request.POST.get("operation")

    if operation == "add":
        result = float(angka1) + float(angka2)
        context = {'result':result}
        return render(request,'blog/kalku.html',context)
    elif operation == "subtract":
        result = float(angka1) + float(angka2)
        context = {'result':result}
        return render(request,'blog/kalku.html',context)
    elif operation == "multiply":
        result = float(angka1) + float(angka2)
        context = {'result':result}
        return render(request,'blog/kalku.html',context)
    elif operation == "devide":
        result = float(angka1) + float(angka2)
        context = {'result':result}
        return render(request,'blog/kalku.html',context)
    else:
         return HttpResponse("calculator.html")


