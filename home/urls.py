
from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.home,name='home'),
    path('delete_shop/<id>/', views.delete_shop,name='delete_shop'),
    path('update_shop/<id>/', views.update_shop,name='update_shop'),
    path('search_shop', views.search_shop,name='search_shop'),
    
]
