from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):  
  #return HttpResponse('<h1>Welcome to Home</h1>')
  #return render(request, 'home.html')
  return render(request, 'home.html', {'name': 'Andres Guerra Montoya'})

