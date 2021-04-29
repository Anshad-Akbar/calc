from django.shortcuts import render

# Create your views here.
def mainFunction(request):
    if request.method == "POST":
        Email=request.POST['email']
        Pass=request.POST['password']
        if((Email=='007anshadah@gmail.com')and(Pass=='12345')):
            print('login success')
        else:
            print('login failed')

                
 
        
        
        return render(request,'main.html')
    return render(request,'main.html')
    
