from django.urls import path
from . import views


urlpatterns=[
    path('',views.details),
    path('/signup', views.signup),
    path('/login', views.login),
    path('/profile',views.profile),
    path('/logout',views.logout),
]