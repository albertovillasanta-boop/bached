from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def carrusel(request):
 return render(request, 'carrusel/main.html')