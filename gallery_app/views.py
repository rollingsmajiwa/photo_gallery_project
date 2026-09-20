from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context = {"name":"Rollings Majiwa"}
    return render(request, "index.html", context)

def contact(request):
    context = {"message":"Contact Us"}
    return render(request, "contact.html", context)

@login_required
def gallery(request):
    context = {"message": "welcome to gallery"}
    return render(request, 'gallery.html', context)