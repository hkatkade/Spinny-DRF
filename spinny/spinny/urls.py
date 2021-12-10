"""spinny URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from store.views import AddBox,ShowBox,EditBox,ShowMyBoxes,DeleteBox

urlpatterns = [
    path('add',AddBox.as_view()),
    path('listAll',ShowBox.as_view()),
    path('listMyBoxes',ShowMyBoxes.as_view()),
    path('edit/<int:pk>',EditBox.as_view()),
    path('delete/<int:pk>',DeleteBox.as_view()),
    path('admin/', admin.site.urls),
]
