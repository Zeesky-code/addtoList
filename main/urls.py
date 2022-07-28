from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name= "index"),
    path('signup',views.signup, name = "signup"),
    path('login', views.loginPage, name="login"),
    path('home', views.home, name = "home"),
    path('logout', views.logout_view, name="logout_view"),
    path("update_grocery", views.update_grocery, name="update_grocery"),
    path("buy/grocery/<int:pk>/", views.buy_grocery, name="buy_grocery"),
    path("delete/grocery/<int:pk>/", views.delete_grocery, name="delete_grocery"),
]

