from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.utils import timezone
from django.core.mail import send_mail

# ! английская версия ==============================================================================================


# def index_eng(request):
#     return render(request, 'blog/eng/index.html')

# def about_us(request):
#     return render(request, 'blog/eng/about_us.html')
    
# def about_our_teacher(request):
#     return render(request, 'blog/eng/about_our_teacher.html')

# def contact_us(request):
#     if request.method == 'POST':
#         message_name = request.POST['message_name']
#         message_email = request.POST['message_email']
#         message = request.POST['message']
#         context = {'message_name':message_name, 'message_email':message_email, 'message':message}
#         send_mail(message_name, message, message_email, ['kimsergey486@gmail.com'])
#         return render(request, "blog/eng/contact_us.html", context)
#     else:   
#         return render(request, "blog/eng/contact_us.html")

# def gallery(request):
#     image = Image.objects.all()
#     paginator = Paginator(image, 23)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog/eng/gallery.html',{'page_obj': page_obj})

# def news(request):  
#     posts = Post.objects.filter(publish=1).order_by('-date')
#     paginator = Paginator(posts, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog/eng/news.html', {'page_obj' : page_obj})

# def post_detail(request, slug):
#     post = Post.objects.get(slug__exact = slug)
#     return render(request, 'blog/eng/post_detail.html', {'post' : post})


# !русская версия ==============================================================================================

# def gallery_ru(request):
#     image = Image.objects.all()
#     paginator = Paginator(image, 25)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog/index_ru.html',{'page_obj': page_obj})

# def news_ru(request):  
#     posts = Post_rus.objects.filter(publish=1).order_by('-date')
#     paginator = Paginator(posts, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog/news_ru.html', {'page_obj' : page_obj})

# def post_detail(request, slug):
#     post = Post.objects.get(slug__exact = slug)
#     return render(request, 'blog/post_detail_ru.html', {'post' : post})

def index_ru(request):
    slider = Carausel.objects.all()
    context = {'slider': slider}
    return render(request, 'blog/index_ru.html', context)

def about_us_ru(request):
    return render(request, 'blog/about_us_ru.html')

# def test(request):
#     return render(request, 'blog/test.html')

def about_our_teacher_ru(request):
    return render(request, 'blog/about_our_teacher_ru.html')

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
