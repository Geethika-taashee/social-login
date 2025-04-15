from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('success')
        else:
            messages.error(request, "Invalid email or password")
    return render(request, 'login.html')

def success(request):
    username = request.user.username
    return render(request, 'success.html', {'username': username})

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')
        user = User.objects.create_user(username=email, email=email, password=password1)
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect('login')  
    return render(request, 'signup.html')

def logout_view(request):
    logout(request) 
    return redirect('login')
