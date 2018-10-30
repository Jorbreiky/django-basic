from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),

    #VISTAS 
    path('', views.post_all, name='post_all'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_detail'),
    path('post/new/', views.post_add, name='post_new'),
    
    #FUNCIONES PARA TEST
    path('page_not_found/', views.page_not_found, name='page_not_found'),
    path('test/', views.test, name='test'),
]