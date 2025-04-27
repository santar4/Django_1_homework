from datetime import datetime
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, CallBackForm, AdminRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Movie

def index(request):
    context = {}
    return render(request, "index.html", context)


def about_us(request):
    context = {}
    return render(request, "about_us.html", context)


def current_datetime(request):
    now = datetime.now()
    html = f''' <html>
        <body>
            <h1>
                Current Datetime: {now}
            </h1>
        </body>
    </html> '''
    return HttpResponse(html, status=200)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Акаунт успішно створений для {form.cleaned_data["username"]}')
            return redirect('index')
        else:
            messages.error(request, 'Помилка у формі')
    else:
        form = RegistrationForm()
    return render(request, "register.html", {'form': form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Дані не вірні')

    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})


def call_back(request):
    if request.method == "POST":
        form = CallBackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Дані успішно відправлені")
            return redirect('call_back_thanks')
        else:
            messages.error(request, 'Дані введено неправильно')
    else:
        form = CallBackForm()
    return render(request, 'call_back.html', context={'form': form})


def call_back_thanks(request):
    return render(request, "call_back_thanks.html")


def register_admin(request):
    if request.method == "POST":
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('index')
    else:
        form = AdminRegistrationForm()
    return render(request, "register_admin.html", context={'form': form})


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, "main_page.html", context={'movies': movies})


def movie_page(request, id):
    movie = Movie.objects.get(pk=id)
    average_rate = Movie.objects.aggregate(average=Avg('rate'))['average']
    return render(request, "movie_page.html", context={'movie': movie, 'average_rate': average_rate})


