from django.urls import path

from . import views

urlpatterns = [
    path('', views.AddressCreateView.as_view(), name='index'),
]