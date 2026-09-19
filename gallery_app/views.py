from django.shortcuts import render

# Create your views here.
def home(request):
    context = {"name":"Rollings Majiwa"}
    return (request, "index.html", context)

def about(request):
    context = {"message":"Welcome to My About"}
    return(request, "about.html", context)