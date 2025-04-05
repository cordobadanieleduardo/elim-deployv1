from django.shortcuts import render

# Create your views here.

def vivianaView(request):
    return render(request,'asesora/home.html')