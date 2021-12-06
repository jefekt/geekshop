"""geekshop URL Configuration

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
from mainapp.views import index, products, contact, context

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('products/', products, name = "products"),
    path('contact/', contact, name = "contact"),
    path('context/', context),
    path('product_all', products, name ="product_all"),
    path('product_home', products, name ="product_home"),
    path('product_office', products, name ="product_office"),
    path('product_modern', products, name ="product_modern"),
    path('product_classic', products, name ="product_classic"),
    path('product_popular', index, name ="product_popular"),
    path('product_new', index, name ="product_new"),


]
