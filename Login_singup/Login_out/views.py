from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Login")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form})

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("Home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})



def Home(request):
    return HttpResponse("You Have Login Successfully----")