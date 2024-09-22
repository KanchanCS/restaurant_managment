from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('<int:item_id>/', views.detail_item, name='detail'),
    path('edit/<int:item_id>/', views.edit_item, name='edit'),
    path('delete/<int:item_id>/', views.delete_item, name='delete'),
    path('add', views.add_item, name='add'),
]