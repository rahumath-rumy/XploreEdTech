from django.urls import path
from. import views

urlpatterns = [
    #path("<int:home_id>/", views.techtool, name="techtool"),
    path('home', views.home, name="Homepage"),
    path('signup', views.signup, name="signup")
]
