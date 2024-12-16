"""
URL configuration for bootstrapproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex1/',ex1,name='ex1'),
    path('ex2/',ex2,name='ex2'),
    path('ex3/',ex3,name='ex3'),
    path('ex4/',ex4,name='ex4'),
    path('ex5/',ex5,name='ex5'),
    path('ex6/',ex6,name='ex6'),
    path('ex7/',ex7,name='ex7'),
    
]
