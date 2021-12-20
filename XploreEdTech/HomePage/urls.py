from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path("<int:home_id>/", views.techtool, name="techtool"),
    path('', views.home, name="Homepage"),
    path('accounts', views.signup, name="accounts"),
    path('getstarted', views.getstarted, name="getstarted"),
    path('profile', views.profile, name="profile"),
    path('login/', views.login_view, name="login"),
    path('logout', views.logoutuser, name="logout"),
    path('about', views.about, name="about"),
    path('donations', views.donations, name="donations"),
    path('upload', views.upload, name="upload"),
    path('worksheet', views.worksheet, name="worksheet"),
    path('checkout', views.checkout, name="checkout"),
    path('register', views.register, name="register"),
]
