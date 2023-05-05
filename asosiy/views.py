# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# from .forms import *
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User

def xabarlar(request):
    if request.user.is_authenticated:
        data = {"xabarlar": Xabar.objects.all()}
        return render(request, "xabarlar.html", data)
    return redirect('/register')
