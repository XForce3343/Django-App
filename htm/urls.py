from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('', views.welcome, name = "welcome"),
        path('login/', views.login, name = "login"),
        path('register/', views.register, name = "register"),
        path('logout/', views.logout, name = "logout"),
        path('admin/', admin.site.urls),
]
