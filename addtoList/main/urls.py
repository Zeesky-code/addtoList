from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name= "index"),
    path('signup',views.signup, name = "signup"),
    path('login', views.loginPage, name="login"),
    path('home', views.home, name = "home"),
    path('logout', views.logout_view, name="logout_view")
]

