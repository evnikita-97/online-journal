from django.urls import path
from . import views


urlpatterns=[
    path('',views.details),
    path('/signup', views.signup),
    path('/login', views.login),
    path('/profile',views.profile),
    path('/logout',views.logout),
    path('/create',views.journal_create),
    path('/list',views.journal_list),
    path('/api/list', views.api_journal_list),
    path('/api/list/view/month/<slug:date>', views.api_journal_list_month),
    path('/api/list/view/day/<slug:date>', views.api_journal_list_day),
]