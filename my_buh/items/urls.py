from django.urls import path

from . import views


app_name = 'items'

urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('create/', views.item_create, name='item_create'),
    path('items/<int:item_id>/edit/', views.item_edit, name='item_edit'),
    path('items/<int:item_id>/delete/', views.item_delete, name='item_delete'),
    path('items/<int:item_id>/sell/', views.item_sell, name='item_sell'),
]
