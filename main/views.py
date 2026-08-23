from django.shortcuts import render, redirect
from main.forms import *

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = MathForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MathForm()
    calculations = Math.objects.all()
    return render(request, 'index.html', {'form' : form, 'calculations' : calculations})