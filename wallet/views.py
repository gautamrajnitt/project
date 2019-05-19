from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'wallet/index.html', {})

def about(request):
    return render(request,'wallet/about.html', {})

def login(request):
    return render(request,'wallet/login.html', {})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
        form = UserCreationForm()
    return render(request,'wallet/Users/register.html', {
        'form': form
        })