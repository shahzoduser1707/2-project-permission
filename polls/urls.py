from django.urls import path
from .views import ListPhoneApiView,DetailUpdateDestroyPhoneView



urlpatterns = [
    path('all/',ListPhoneApiView.as_view()),
    path('detail/<int:pk>',DetailUpdateDestroyPhoneView.as_view())
]