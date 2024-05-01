from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.template import context


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success_url')
        else:
            pass
    return render(request, 'registration/login.html', context)


def custom_logout(request):
    logout(request)
    return redirect('success_url')
