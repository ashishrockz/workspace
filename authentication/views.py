from django.shortcuts import render
def login(request):
 return render(request, "login")
# Create your views here.
def signup(request):
 return render(request, "signup")