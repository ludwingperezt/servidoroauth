"""ejemplooauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

#endpoint de prueba de la API
from api.views import ApiEndpoint
from otros.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')), #endpoints del servidor oauth
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login.html'), name="login"), #endpoint de login
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name="logout"), #endpoint de logout
    url(r'^api/hello', ApiEndpoint.as_view()), #endpoint de ejemplo de la api

    #endpoints de ejemplo de acceso
    url(r'^secret$', secret_page, name='secret'),
    url(r'^secreta$', secreta, name='secreta'),

    url(r'^drf/', include('ejemplodrf.urls')),
]
