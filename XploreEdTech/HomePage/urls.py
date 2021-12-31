from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("<int:home_id>/", views.techtool, name="techtool"),
    path('', views.home, name="Homepage"),
    path('accounts', views.register, name="accounts"),
    path('profile', views.profile, name="profile"),
    path('login/', views.login_view, name="login"),
    path('logout', views.logoutuser, name="logout"),
    path('about', views.about, name="about"),
    path('donations', views.donations, name="donations"),
    path('upload', views.upload, name="upload"),
    path('worksheet', views.worksheet, name="worksheet"),
    path('search', views.wksearch, name="search"),
    path('searchtool', views.toolsearch, name="searchtool"),
    path('edtechtool', views.ctoolsearch, name="edtechtool"),
    path('common', views.commontools, name="common"),
    path('math', views.mathtool, name="math"),
    path('science', views.sciencetool, name="science"),
    path('language', views.langtool, name="language"),
    path('preschool', views.preschooltool, name="preschool"),
    path('payment', views.payment.as_view(), name="payment"),
    path('charge/', views.charge, name='charge'),


    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done", auth_views.PasswordResetCompleteView.as_view(template_name='password_change_done.html'),
         name="password_reset_done"),
    path("reset/<uid64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password_change/done", auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name="password_change_complete"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name="password_change_complete"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name="password_reset_complete"),
]
