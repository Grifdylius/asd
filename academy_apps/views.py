from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail


def index_ru(request):
    slider = Carausel.objects.all()
    context = {'slider': slider}
    return render(request, 'blog/index_ru.html', context)

def contact_us_ru(request):
    if request.method == 'POST':
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        context = {'message_name':message_name, 'message_email':message_email, 'message':message}
        send_mail(message_name, message, message_email, ['kimsergey486@gmail.com'])
        return render(request, "blog/contact_us_ru.html", context)
    else:   
        return render(request, "blog/contact_us_ru.html")
