from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Record, Status, Type, Category, SubCategory
from .serializers import RecordSerializer, StatusSerializer, TypeSerializer, CategorySerializer, SubCategorySerializer


# Create your views here.





# --------------------- API ---------------------


class RecordFilter(filters.FilterSet):
    data_created = filters.DateFromToRangeFilter()

    class Meta:
        model = Record
        fields = ['data_created', 'status', 'type', 'category', 'subcategory']


class RecordApiView(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    http_method_names = ['get', 'post', "put" ,'delete']
    filter_backends = [DjangoFilterBackend]  
    filterset_class = RecordFilter

class StatusApiView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    http_method_names = ['get', 'post', "put" ,'delete']

class TypeApiView(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    http_method_names = ['get', 'post', "put" ,'delete']

class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', "put" ,'delete']

class SubCategoryApiView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    http_method_names = ['get', 'post', "put" ,'delete']