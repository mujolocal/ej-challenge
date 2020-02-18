from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect


# global users list required to have multiple users since i decidedto use the django.contrib.auth.models User class to create and login  users because generally users are stored in a cookie maybe session tokens may work better but this works for now
users = []



def start_game(request):
    return render(request, "game/start_game.html", {})

def player_1(request):
    global users
    if request.method == "POST":
        user_name = request.POST["name"]
        password = request.POST["password_1"]
        # future: username and password need to be cleaned
        user1 = authenticate(username=user_name, password=password)
        if user1 is not None:
            users.append(user1)
            return HttpResponseRedirect('/player_2')
    return render(request, "game/player_1.html", {})

def player_2(request):
    global users
    if request.method == "POST":
        user_name = request.POST["name"]
        password = request.POST["password_1"]
        # Future:username and password need to be cleaned
        user2 = authenticate(username=user_name, password=password)
        # future: insure users arent the same
        if user2 is not None:
            users.append(user2)
            return HttpResponseRedirect('/game')
    return render(request, "game/player_2.html", {})

def game(request):
    global users
    context ={"users":users}
    return render(request, "game/game.html", context)

def complete_game(request, username):

    remove_users()
    return render(request, "game/complete_game.html",{"username":username})

def logout(request):
    remove_users()
    return render(request, "game/logout.html")

def remove_users():
    """
    remove all users from global and log users out
    """
    global users
    users = []



def create_player(request):
    if request.method == "POST":
        user_name = request.POST["name"]
        password = request.POST["password_1"]
        # username and password need to be cleaned
        user = User.objects.create_user(username=user_name, password=password)

        return HttpResponseRedirect('/')
    return render(request, "game/create_player.html", {})
