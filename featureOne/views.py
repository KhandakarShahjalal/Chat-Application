from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homeone.html',{'name' : 'featureOne'})

def aboutus(request):
    return render(request,'aboutus.html')