from django.shortcuts import render, redirect
from projects_app.models import FormProject
from Form.models import message
from django.http import HttpResponse
from django.contrib import messages


def show_home(request):
    
    success_message = None
    error_message = None
    if request.method == "POST":
        try:
            # دریافت داده‌ها
            conName = request.POST.get('conName', '').strip()
            conLName = request.POST.get('conLName', '').strip()
            conEmail = request.POST.get('conEmail', '').strip()
            conPhone = request.POST.get('conPhone', '').strip()
            conMessage = request.POST.get('conMessage', '').strip() 
            
            # اعتبارسنجی فیلدهای اجباری
            if not conName or not conEmail or not conMessage:
                return render(request, 'index.html', {
                    'error': 'لطفاً تمام فیلدهای اجباری را پر کنید'
                })
            
            # ذخیره در دیتابیس
            message.objects.create(
                conName=conName,
                conLName=conLName,
                conEmail=conEmail,
                conPhone=conPhone,
                conMessage=conMessage
            )
            success_message = 'پیام شما با موفقیت ارسال شد!'
           
            
        except Exception as e:
            error_message = 'خطا در ارسال پیام'
            
    formproject = FormProject.objects.all()
    return render(request , 'index.html' , context={'formproject' : formproject ,'success_message': success_message , 'error_message': error_message,} )
        
        
    
