"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from auto.views import *

urlpatterns = [
    path('auto/', include('auto.urls')),
    path('admin/', admin.site.urls),
    path('api/carlist/', CarAPIList.as_view()),
    path('api/carlist/<int:pk>/', CarAPIUpdate.as_view()),
    path('api/carsettings/<int:pk>/', CarAPIDetailView.as_view()),
    path('api/countrylist/', CountryAPIList.as_view()),
    path('api/countrylist/<int:pk>/', CountryAPIUpdate.as_view()),
    path('api/countrysettings/<int:pk>/', CountryAPIDetailView.as_view()),
    path('api/partlist/', PartAPIList.as_view()),
    path('api/partlist/<int:pk>/', PartAPIUpdate.as_view()),
    path('api/partsettings/<int:pk>/', PartAPIDetailView.as_view()),
]
