from __future__ import unicode_literals
from models import Friend
from ..login_app.models import User
from django.contrib import messages
from django.shortcuts import render, redirect


def dashboard(request):
    if "first_name" not in request.session:
        return redirect("/")
    context={
        'user':User.objects.get(id=request.session['id']).first.all(),
        'other_users':User.objects.exclude(id=request.session['id'])
    }
    return render(request, "second_app/dashboard.html", context)

def addFriend(request, id):


    test = User.objects.get(id=id)
    test2 = User.objects.get(id = id)

    Friend.objects.create(user_friend = test, second_friend = test2)
    return redirect("/second_app/dashboard")

def showUser(request, id):
    context={
        'user':User.objects.get(id=id),
    }
    return render(request, "second_app/show.html", context)
    
def deletePet(request, id):
    User.objects.get(id=id).delete()
    return redirect("/second_app/dashboard")

def home(request):
    return redirect("/second_app/dashboard")
