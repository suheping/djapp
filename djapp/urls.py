"""djapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from autotest import views as at_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',at_views.index),
    path('index/',at_views.index),
    path('login/',at_views.login),
    path('reg/',at_views.reg),
    path('uploadConf/',at_views.uploadConf),
    path('uploadDatafile/',at_views.uploadDatafile),
    path('runtest/',at_views.runtest),
    path('logout/',at_views.logout),
    path('download_conf/',at_views.download_conf),
    path('download_api',at_views.download_api),
    path('download_process',at_views.download_process),
]
