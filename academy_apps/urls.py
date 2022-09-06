from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_ru, name = 'index_ru'),
    path('contact/', views.contact_us_ru, name = 'contact_us_ru'),
]
