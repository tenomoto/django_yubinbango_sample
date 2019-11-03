from django.urls import path

from . import views

urlpatterns = [
    path('', views.AddressListView.as_view(), name='index'),
    path('create', views.AddressCreateView.as_view(), name='create'),
]