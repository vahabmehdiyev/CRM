from django.urls import path
from .views import CustomerListView, CustomerDetailView

urlpatterns = [
    path('', CustomerListView.as_view(), name='customers'),
    path('customer/<int:pk>', CustomerDetailView.as_view(), name='customer-detail'),
    
    
]