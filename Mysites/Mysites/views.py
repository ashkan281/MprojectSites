from django.shortcuts import render
from django.http import HttpResponse
from projects_app.models import FormProject
from Form.models import message


def show_home(request):    
    
    if request.method == "POST":
        name = request.POST.get('name')
        namefamily = request.POST.get('namefamily')
        email = request.POST.get('email')
        number = request.POST.get('number')
        sub = request.POST.get('sub')
        message.objects.create(name=name , namefamily=namefamily , email=email , number=number , sub=sub)
    
    
    
    formproject = FormProject.objects.all()
    return render(request , 'index.html' , context={'formproject' : formproject})

