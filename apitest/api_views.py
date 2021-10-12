from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import connection

from apitest.models import ApiTest, ApiStep, Apis

# Create your views here.


def test(request):
    return HttpResponse("hello world")


def login(request):
    # return render(request, "login.html")
    if request.POST:
        # username, password = "", ""
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            request.session["user"] = username
            request.session["is_login"] = True
            return HttpResponseRedirect("/home/")
        else:
            return render(request, "login.html", {"error": "username or password error"})
    return render(request, "login.html")


def home(request):
    return render(request, "home.html")


def logout(request):
    auth.logout(request)
    return render(request, "login.html")

# 接口管理
@login_required
def apitest_manage(request):
    apitest_list = ApiTest.objects.all()
    username = request.session.get("user", "")
    return render(request, "apitest_manage.html", {"user":username, "api_tests": apitest_list})


# 接口步骤管理
@login_required
def apistep_manage(request):
    username = request.session.get("user", "")
    apistep_list = ApiStep.objects.all()
    return render(request, "apistep_manage.html", {"user": username, "api_steps": apistep_list})

# 单一接口管理
@login_required
def apis_manage(request):
    username = request.session.get("user", "")
    apis_list = Apis.objects.all()
    return render(request, "apis_manage.html", {"user": username, "apis": apis_list})


@login_required
def test_report(request):
    username = request.session.get("user", "")
    api_list = Apis.objects.all()
    api_counts = api_list.count()

    # 直接用filter是最简单的
    api_success_counts = Apis.objects.filter(api_status=1).count()
    api_fail_counts = Apis.objects.filter(api_status=0).count()

    # # 用connection去执行原始sql
    # with connection.cursor() as cursor:
    #     cursor.execute("select count(id) from apitest_apis where api_status==0")
    #     api_fail_counts = cursor.fetchone()[0]
    #     cursor.execute("select count(id) from apitest_apis where api_status==1")
    #     api_success_counts = cursor.fetchone()[0]

    # # 这个写法有点蠢，获取raw会返回RawQuerySet实例，需要用迭代获取对象信息
    # api_fail_counts, api_success_counts = 0, 0
    # for api in Apis.objects.raw("select id, count(id) as fail_count from apitest_apis where api_status==0"):
    #     api_fail_counts = api.fail_count
    #     break
    # for api in Apis.objects.raw("select id, count(id) as success_count from apitest_apis where api_status==1"):
    #     api_success_counts = api.success_count
    #     break

    return render(request, "report.html", {"user": username, "api_list": api_list, "api_counts": api_counts,
                                           "api_success_counts": api_success_counts, "api_fail_counts": api_fail_counts})


