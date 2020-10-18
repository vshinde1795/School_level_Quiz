import pyautogui as pu
from django.shortcuts import render,redirect
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username=username1, password=password1)
        print("user",user)
        if user is not None:
            auth.login(request, user)
            pu.confirm("Login Successful.")
            return redirect('create_quiz/')
        else:
            pu.alert("Please enter correct Username or password.")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')