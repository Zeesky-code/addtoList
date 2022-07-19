from django.shortcuts import render, redirect
from .forms import signupForm, loginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    
    form = signupForm()
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'signup.html', context)

def loginPage(request):
    if request.method == 'POST':
        form = loginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password )

        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")
		


    form = loginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def home(request):
    return render (request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect ('index')
def error_404_view(request, exception):
    return render(request, '404.html', status=404)