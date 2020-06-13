from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register', views.reg),
    path('login', views.login),
    path('login/emailVerify',views.emailVerify),
    path('about',views.about),
    path('application-form',views.application),
]
