from django.urls import path
from. import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path("<int:home_id>/", views.techtool, name="techtool"),
    path('', views.home, name="Homepage"),
    path('accounts', views.signup, name="accounts"),
    path('profile', views.profile, name="profile"),
    path('login/', views.login_view, name="login")
]

