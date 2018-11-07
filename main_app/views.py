from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound,HttpResponse
from django.contrib.auth import authenticate, login,logout
from .form import LoginForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def index(request):
    islogin=request.user.is_authenticated
    send={"islogin":islogin}
    return render(request,"index.html",send)

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
    return render(request, 'register.html', {'form': form})

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
            return render(request, 'login.html', {'form': form , 'error':"نام کاربری یا رمز عبور نادرست است"})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form , 'error':'' })
@login_required
def Profile(request):
    userdict = {'textcolor':'#2b5b84',
    'degree':'کاربر عادی',
    'name':'جنگو پایتونی نژاد',
    'username' : 'djangopy',
    'bio':'اسم بابام پایتونه که یه گوگلی ساختتش و علاقه به طراحی سایت دارم',
    'age': '43',
    'bio':'اسم بابام پایتونه که یه گوگلی ساختتش و علاقه به طراحی سایت دارم',
    'skills':'پایتون - جنگو - C++ , C ',
    'city':'Tehran',
    'score':24,
    }

    return render(request,  'profile.html',userdict)
@login_required
def logouty(request):
    logout(request)

    return redirect('profile')
context = {"titlepre":"فعلا یه صفحه ورود و یه صفحه ثبت نام داریم",
"copyright":"انجمن پایتون python.com (C) 2018 " , }
