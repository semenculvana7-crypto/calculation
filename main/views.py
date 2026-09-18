from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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

def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        age = request.POST['age']
        description = request.POST['description']

        user = User.objects.create_user(
            password=password,
            username=username
        )

        Profile.objects.create(
            user=user,
            name=username,
            description=description,
            age=age
        )

        return redirect('index')

    return render(request, 'register.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('index')

        return render(request, 'login.html', {
            'error': 'Неверный логин или пароль'
        })

    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')