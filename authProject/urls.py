"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from authApp import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authApp.views.checkDetailView import CheckDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userCreate/',views.UserCreateView.as_view()),
    path('userDetail/<int:pk>',views.UserDetailView.as_view()),
    path('refreshToken/',TokenRefreshView.as_view()),
    path('loginUser/',TokenObtainPairView.as_view()),
    path('productCreate/',views.ProductCreateView.as_view()),
    path('productDetail/<int:pk>',views.ProductDetailView.as_view()),
    path('productUpdate/<int:pk>',views.ProductUpdateView.as_view()),
    path('productDelete/<int:pk>',views.ProductDeleteView.as_view()),
    path('checkCreate/',views.CheckCreateView.as_view()),
    path('checkDetail/<int:pk>',views.CheckDetailView.as_view())

]

