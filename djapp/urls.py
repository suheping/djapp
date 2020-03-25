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
# 导入辅助函数get_schema_view
from rest_framework.schemas import get_schema_view
# 导入两个类
from rest_framework_swagger.renderers import SwaggerUIRenderer,OpenAPIRenderer

# 利用辅助函数引入所导入的两个类
schema_view = get_schema_view(title='API',renderer_classes=[SwaggerUIRenderer,OpenAPIRenderer])

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
    path('testapi/',at_views.testapi),
    path('docs/',schema_view),   # 配置docs的url路径
]
