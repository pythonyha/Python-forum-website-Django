from django.shortcuts import render

def index(request):
     return render(request,"index.html",context)

def register(request):
     return render(request,"register.html",context)

def login(request):
     return render(request,"login.html",context)

context = {"titlepre":"فعلا یه صفحه ورود و یه صفحه ثبت نام داریم",
"copyright":"انجمن پایتون python.com (C) 2018 "}
