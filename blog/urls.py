from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),

    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    path('page_not_found/', views.page_not_found, name='page_not_found'),
]