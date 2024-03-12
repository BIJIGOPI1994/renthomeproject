"""
URL configuration for real project.

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
from django.urls import path
from renthome import views
app_name="renthome"


urlpatterns =   [
    path('',views.index,name='index'),
    path('renthome.html',views.renthome,name='renthome'),
    path('rentflat.html',views.rentflat,name='rentflat'),
    path("register",views.register,name='register'),
    path('login.html',views.user_login,name='user_login'),
    # path('blog.html',views.blog,name='blog'),
    path('gallery.html',views.gallery,name='gallery'),
    path('details.html/<p>',views.details,name='details'),
    path('category',views.allcategories,name='allcat'),
    path('property/<p>',views.allproperty,name="allproperty"),
    path("logout",views.user_logout,name="logout"),
    path('contact',views.contact,name='contact'),
    
    
    ]


