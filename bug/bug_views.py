from django.shortcuts import render
from bug.models import Bug


# Create your views here.
def bug_manage(request):
    user_name = request.session.get("user", "")
    bug_list = Bug.objects.all()
    return render(request, "bug_manage.html", {"user": user_name, "bugs": bug_list})
