from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def error_404_view(request, exception):
    return render(request, '404.html', status=404)