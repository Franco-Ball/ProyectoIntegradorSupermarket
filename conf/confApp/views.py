from django.shortcuts import render

# Create your views here.
def home_screen_view(request):

    return render(request, "base.html")

def signin_screen_view(request):
    return render(request, "signin.html")

def cajeros_view(request):
    return render(request, "cajeros/base.html")