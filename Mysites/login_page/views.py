from django.shortcuts import render

# Create your views here.


def show_login(request):
    return render(request , 'login_page/login.html' , context={})

