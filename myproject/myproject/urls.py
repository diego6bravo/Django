"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic import RedirectView # Agrego esta línea para declarar RedirectView que sirve para redirigir

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('newapp/', include('newapp.urls', namespace='newapp')),
    path('', RedirectView.as_view(url='/myapp/')) # Agrego esta línea para redirigir a myapp/ en caso de que escriba directamente la raíz de la URL, porque sino sale error 404 en la raíz
]

handler404 = 'myproject.views.handler404'