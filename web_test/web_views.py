from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from web_test.models import WebCase, WebCaseStep


# Create your views here.
@login_required
def web_case_manage(request):
    list_display = WebCase.objects.all()
    user_name = request.session.get("user", "")
    return render(request, "web_case_manage.html", {"user": user_name, "web_case_list": list_display})


@login_required
def web_case_step_manage(request):
    list_display = WebCaseStep.objects.all()
    user_name = request.session.get("user", "")
    return render(request, "web_case_step_manage.html", {"user": user_name, "web_case_step_list": list_display})

