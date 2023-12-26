"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from listings import views

urlpatterns = [
    

    path('admin/', admin.site.urls),


    path('about/', views.about, name= 'about'),

    path('contact-us/', views.contact, name='contact'),

    path('confirm-email/', views.email_sent, name='email-sent'),


    path('bands/<int:id>/', views.band_detail, name='band-detail'),

    path('bands/add/', views.band_create, name='band-create'),

    path('bands/<int:id>/delete', views.band_delete, name='band-delete'),

    path('bands/<int:id>/update', views.band_update, name='band-update'),

    path('bands/', views.band_list, name = 'band-list'),


    path('listings/', views.listing_list, name = 'listing-list'),

    path('listings/add/', views.listing_create, name='listing-create'),

    path('listings/<int:id>/update', views.listing_update, name='listing-update'),

    path('listings/<int:id>/delete', views.listing_delete, name='listing-delete'),

    path('listings/<int:id>/', views.listing_detail, name='listing-detail'),



    path('deserts/', views.desert_list, name = 'desert-list'),

    path('deserts/add/', views.desert_create, name='desert-create'),

    path('deserts/<int:id>/update', views.desert_update, name='desert-update'),

    path('deserts/<int:id>/delete', views.desert_delete, name='desert-delete'),

    path('deserts/<int:id>/', views.desert_detail, name='desert-detail'),

    path('home/', views.home, name='home'),
    
    path('chat/', views.chat, name='chat'),

    path('chat/delete/<int:chat_id>/', views.delete_chat, name='delete_chat'),
]
