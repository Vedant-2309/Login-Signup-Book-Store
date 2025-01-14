from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        else:
            try:
                # Create a superuser
                user = User.objects.create_superuser(username=username, email=email, password=password)
                messages.success(request, "Superuser account created successfully!")
                return redirect('bookapp/landing_page.html')  # Redirect to the login page or another page
            except Exception as e:
                messages.error(request, f"Error creating superuser: {e}")

    return render(request, 'bookapp/login.html')

def landing(request):
    return render(request, 'bookapp/landing_page.html')

