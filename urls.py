from django.urls import path
from . import views

urlpatterns = [
    # path('eng/', views.index_eng, name = 'index_eng'),
    # path('about/', views.about_us, name = 'about_us'),
    # path('about_our_teacher/', views.about_our_teacher, name = 'about_our_teacher'),
    # path('contact/', views.contact_us, name = 'contact_us'),
    # path('news/', views.news, name = 'news'),
    # path('post_detail/<slug:slug>/', views.post_detail, name = 'post_detail_url'),
    # ! русская версия
    # path('gallery/', views.gallery_ru, name = 'gallery_ru'),
    # path('news/', views.news_ru, name = 'news_ru'),
    # path('post_detail/<slug:slug>/', views.post_detail, name = 'post_detail_url'),
    # path('about/', views.about_us_ru, name = 'about_us_ru'),
    # path('test/', views.test, name = 'test'),
    
    
    
    path('', views.index_ru, name = 'index_ru'),
    path('about_our_teacher/', views.about_our_teacher_ru, name = 'about_our_teacher_ru'),
    path('contact/', views.contact_us_ru, name = 'contact_us_ru'),
]
