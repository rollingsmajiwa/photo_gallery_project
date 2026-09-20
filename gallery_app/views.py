from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ContactMessage

# Create your views here.
def home(request):
    context = {"name":"Rollings Majiwa"}
    return render(request, "index.html", context)

def contact(request):
    context = {"message":"Contact Us"}
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
    # saving to database
        ContactMessage.objects.create(
            first_name = first_name,
            email= email,
            message=message
        )
        return render(request, "contact.html", {'success': True})
    return render(request, "contact.html", context)

@login_required
def gallery(request):
    context = {"message": "welcome to gallery"}
    return render(request, 'gallery.html', context)