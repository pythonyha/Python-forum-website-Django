from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound,HttpResponse
from django.contrib.auth import authenticate, login
from .form import LoginForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def index(request):
     return render(request,"index.html",context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'mylogin.html', {'form': form})
@login_required
def Profile(request):
    HttpResponse("You Are Log IN IN Profile")
context = {"titlepre":"فعلا یه صفحه ورود و یه صفحه ثبت نام داریم",
"copyright":"انجمن پایتون python.com (C) 2018 "}
