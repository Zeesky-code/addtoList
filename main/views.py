from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import signupForm, loginForm
from .models import Grocery
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf  import csrf_protect
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
        # "new-grocery" is the name of the input in the file
        if request.POST.get("new-grocery"):
            grocery_name = request.POST.get("new-grocery")
            grocery = Grocery.objects.create(name=grocery_name, user=request.user)
            grocery.save()
            return redirect("home")
        else:
            formerror = "Oops, please enter a Grocery!!"

    groceries = Grocery.objects.filter(user = request.user, bought = False)

    # paginating 6 items per page
    paginator = Paginator(groceries, 6)
    
    # It's URL param for getting the current page number
    page_number = request.GET.get("page")
    
    # retrieving all the todo items for that page
    page_obj = paginator.get_page(page_number)
   
    #get Categories
    categories = Grocery.Category_choices

    context = {"groceries":groceries, "page_obj": page_obj, "categories": categories}
    return render (request, 'main.html', context)

def update_grocery(request, pk):
    # NOTE: below get_object_or_404() returns a data if exists else status 404 not found
    grocery = get_object_or_404(Grocery, id=pk, user=request.user)

    # NOTE: request.POST.get("grocery_{pk}") is the input name of the grocery modal
    if request.method == "POST":
        grocery.name = request.POST.get(f"grocery_name")
        print(grocery.name)
        grocery.category = request.POST.get(f"grocery_category")
        grocery.quantity = request.POST.get(f"grocery_quantity")
        grocery.price = request.POST.get(f"grocery_price")
        grocery.note =  request.POST.get(f"grocery_note")

        grocery.save()
        print(grocery)
        # return to the home page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

def delete_grocery(request, pk):
    #delete item    
    grocery = get_object_or_404(Grocery, id=pk, user=request.user)
    grocery.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def buy_grocery(request, pk):
    #Updating todo as completed item
    grocery = get_object_or_404(Grocery, id=pk, user=request.user)
    grocery.bought = True
    grocery.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def logout_view(request):
    logout(request)
    return redirect ('index')

def error_404_view(request, exception):
    return render(request, '404.html', status=404)