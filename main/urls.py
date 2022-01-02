from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('login', views.login_view, name='main_login'),
    path('logout', views.logout_view, name='main_logout'),
    path('create-account', views.create_account, name="main_create_account")
]
