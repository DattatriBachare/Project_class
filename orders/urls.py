from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('add_address/', views.add_address, name='add_address'),
    path('select_address/<int:order_id>/', views.select_address_for_order, name='select_address'),
]