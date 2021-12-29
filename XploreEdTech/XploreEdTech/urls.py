"""XploreEdTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('allauth.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('', include("HomePage.urls")),
                  path('profile/', include("HomePage.urls")),
                  path('login/', include("HomePage.urls")),
                  path('about/', include("HomePage.urls")),
                  path('donations', include("HomePage.urls")),
                  path('checkout', include("HomePage.urls")),
                  path('upload', include("HomePage.urls")),
                  path('worksheet', include("HomePage.urls")),
                  path('search', include("HomePage.urls")),
                  path('searchtool', include("HomePage.urls")),
                  path('common', include("HomePage.urls")),
                  path('math', include("HomePage.urls")),
                  path('language', include("HomePage.urls")),
                  path('payment', include("HomePage.urls")),

                  # path('logout', include("django.contrib.auth.urls")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
