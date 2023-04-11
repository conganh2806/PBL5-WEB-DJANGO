"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Authentication import views
from Setting import settingViews
from Profile import profileViews
from AddClass import addClassViews
from HomeApp import homeViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginSignUp),
    path('postsignUp/', views.postSignUp),
    path('postsignIn/', views.postSignIn),
    path('setting/', homeViews.goToSetting, name="setting"),
    path('postUpdate/', settingViews.postUpdate),
    path('homepage/', settingViews.postCancel, name="homepage"),
    path('addClass/', homeViews.AddClass, name="addClass"),
    path('', views.logOut, name="log"),
    path('profile/', profileViews.profile, name="profile"),
    
]
