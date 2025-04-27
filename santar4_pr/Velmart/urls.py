from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("date/", views.current_datetime, name="date"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("call_back/", views.call_back, name="call_back"),
    path("call_back_thanks/", views.call_back_thanks, name="call_back_thanks"),
    path('register_admin/', views.register_admin, name='register_admin'),
    path('movies/', views.movies_list, name='movies_list'),
    path('movie/<int:id>/', views.movie_page, name='movie_page'),
]