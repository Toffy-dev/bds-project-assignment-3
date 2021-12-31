"""fastfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from customer import views as cv
from employee import views as ev
from transaction import views as tv
from detailview import views as dv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', cv.register, name='register'),
    path('', include('main.urls')),
    path('', include('django.contrib.auth.urls')),

    path('emplist/', ev.index, name='emplist'),
    path('addnew',ev.addnew, name='addnew'),  
    path('edit/<int:id>', ev.edit, name='edit'),  
    path('update/<int:id>', ev.update, name='update'),  
    path('delete/<int:id>', ev.destroy, name='delete'),

    path('transaction/', tv.process_payment, name='process_payment'),

    path('orderview/', dv.order, name='orderview')

]