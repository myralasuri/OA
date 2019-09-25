"""OA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from employee import views

urlpatterns = [
    path('', views.home),
    path("OA/emp/<int:id>/", views.emp, name="emp"),
    path("OA/emp/<int:id>/newleave", views.newleave, name=""),
    path("OA/manager/<int:id>/", views.manager, name="manager"),
    path("OA/manage/leave/<int:id>/", views.approval, name="manage"),
    path('admin/', admin.site.urls),
]
