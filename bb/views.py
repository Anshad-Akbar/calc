from django.shortcuts import render

# Create your views here.
def mainFunction(request):
    return render(request,'main.html')
    
