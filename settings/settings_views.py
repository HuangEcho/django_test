from django.shortcuts import render
from django.contrib.auth.models import User
from settings.models import Settings


# Create your views here.
def setting_manage(request):
    user_name = request.session.get("user", "")
    setting_list = Settings.objects.all()
    return render(request, "setting_manage.html", {"user": user_name, "settings": setting_list})


def setting_user(request):
    user_list = User.objects.all()
    user_name = request.session.get("user", "")
    return render(request, "setting_user.html", {"user_list": user_list, "user_name": user_name})
