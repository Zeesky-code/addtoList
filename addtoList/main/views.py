from django.shortcuts import render, redirect
from .forms import signupForm, loginForm
from .models import Grocery
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


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

@login_required
def home(request):
    model = Grocery
    if request.method == 'POST':
        # "new-todo" is the name of the input in crud.html file
        grocery_name = request.POST.get("new-grocery")
        grocery = Grocery.objects.create(name=grocery_name, user=request.user)
        return redirect("home")

    groceries = Grocery.objects.filter(user = request.user, bought = False)

    # paginating 10 items per page
    paginator = Paginator(groceries, 10)
    
    # It's URL param for getting the current page number
    page_number = request.GET.get("page")
    
    # retrieving all the todo items for that page
    page_obj = paginator.get_page(page_number)


    context = {"groceries":groceries, "page_obj": page_obj}
    return render (request, 'dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect ('index')

def error_404_view(request, exception):
    return render(request, '404.html', status=404)