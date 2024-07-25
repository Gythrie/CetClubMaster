from django.shortcuts import render , HttpResponse

def home(request):
    # return render(request,'home.html')
    return render(request , 'home.html')

# Create your views here.
