from django.shortcuts import render, redirect
from unicodedata import category
from main.models import *
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
    calculations = Math.objects.last()

    category_id = request.GET.get('category')

    if category_id:
        history = Math.objects.filter(category=category_id)
    else:
        history = Math.objects.none()

    categories = Category.objects.all()
    return render(request, 'index.html', {
        'form': form,
        'calculations': calculations,
        'history': history,
        'categories': categories,
    })