from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from .models import PhoneModel
from .serializer import PhoneSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permission import OwnerPermission
# Create your views here.

class ListPhoneApiView(generics.ListAPIView):
    queryset = PhoneModel.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = (IsAuthenticated,OwnerPermission)


class DetailUpdateDestroyPhoneView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneModel.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = (IsAuthenticated,OwnerPermission)