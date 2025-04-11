from django.urls import path

from . import views

urlpatterns = [
    path('',  views.home_page, name='home'),
    path('lists/<int:pk>/', views.view_list, name='view_list'),
    path('lists/new/', views.new_list, name='new_list'),
    path('lists/<int:pk>/add_item/', views.add_item, name='add_item')
]






