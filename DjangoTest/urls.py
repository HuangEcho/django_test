"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from apitest import api_views
from product import product_views
from bug import bug_views
from settings import settings_views
from app_test import app_test_views
from web_test import web_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("test/", api_views.test),
    path("login/", api_views.login),
    path("home/", api_views.home),
    path("logout/", api_views.logout),
    path("product_manage/", product_views.product_manage),
    path("apitest_manage/", api_views.apitest_manage),
    path("apistep_manage/", api_views.apistep_manage),
    path("apis_manage/", api_views.apis_manage),
    path("report/", api_views.test_report),
    path("bug_manage/", bug_views.bug_manage),
    path("setting_manage/", settings_views.setting_manage),
    path("user/", settings_views.setting_user),
    path("app_case/", app_test_views.app_case_manage),
    path("app_case_step/", app_test_views.app_case_step_manage),
    path("web_case/", web_views.web_case_manage),
    path("web_case_step/", web_views.web_case_step_manage),

]
