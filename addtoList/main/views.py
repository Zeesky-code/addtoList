from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import signupForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    
    form = signupForm()
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'signup.html', context)

def error_404_view(request, exception):
    return render(request, '404.html', status=404)