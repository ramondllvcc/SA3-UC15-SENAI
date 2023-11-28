from django.contrib import admin
from django.urls import path
from app_sa3 import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home, name= "home"),
    
    path('cadastro/', views.cadastro, name= "cadastro"),

    path('login/', views.login, name= "login")
]

staticfiles_urlpatterns = staticfiles_urlpatterns()
