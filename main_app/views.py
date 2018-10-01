from django.shortcuts import render

def index(request):
     return render(request,"index.html",context)

def register(request):
     return render(request,"register.html")

def login(request):
     return render(request,"login.html")
context = {"titlepre":"فعلا یه صفحه ورود و یه صفحه ثبت نام داریم"}
