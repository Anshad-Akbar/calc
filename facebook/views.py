from django.shortcuts import render

# Create your views here.
def fbFunction(request):
    return render(request,'fb.html')
def calcFunction(request):
    return render(request,'calc.html')