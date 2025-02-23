"""
URL configuration for condominio project.

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
from django.conf import settings
# Use static() to add URL mapping to serve static files during development (only)
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("gestion_capital/", include("gestion_capital.urls")),
    path("iniciarSesion/", include("iniciarSesion.urls")),
    ] + static(settings.STATIC_URL)

urlpatterns += [path('gestion_propietario/', include('gestion_propietario.urls'))]
