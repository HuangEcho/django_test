from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from app_test.models import AppCase, AppCaseStep


# Create your views here.
# app用例管理
@login_required
def app_case_manage(request):
    app_case_list = AppCase.objects.all()
    user_name = request.session.get("user", "")
    return render(request, "app_case_manage.html", {"user": user_name, "app_cases": app_case_list})


# app用例测试步骤
@login_required
def app_case_step_manage(request):
    app_case_step_list = AppCaseStep.objects.all()
    user_name = request.session.get("user", "")
    return render(request, "app_case_step_manage.html", {"user": user_name, "app_case_steps": app_case_step_list})
