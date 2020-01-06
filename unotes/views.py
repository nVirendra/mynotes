from django.contrib import messages
from .models import Unote
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Welcome this is your dashboard')
            return redirect('dashboard')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/')
    else:
        return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'it is taken signup again with different username.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.info(request, 'Successfully Register Login To Continue')
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('/')
    else:
        return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def addnotes(request):
    if request.method == "POST":
        file_name = request.POST.get('file_name', '')
        file_desc = request.POST.get('file_desc', '')
        file = request.POST.get('file', '')
        unote = Unote(file_name=file_name, file_desc=file_desc, file=file)
        unote.save()
    return render(request, 'addnotes.html')
