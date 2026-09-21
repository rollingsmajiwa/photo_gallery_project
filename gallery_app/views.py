from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ContactMessage, Photo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    photos = Photo.objects.all()
    context = {"message":"Discover visual stories, landscape views, and creative moments.", "photos": photos}
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
    photos = Photo.objects.all()
    context = {"message": "welcome to my Gallery", "photos": photos}
    return render(request, 'gallery.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the user after signup
            return redirect('gallery')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})