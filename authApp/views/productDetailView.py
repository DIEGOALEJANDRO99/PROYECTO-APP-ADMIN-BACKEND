
from django.conf import settings
from django.db.models.query import QuerySet
from django.http import response
from django.http.response import ResponseHeaders
from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from authApp.models.product import Product

from authApp.serializers.productSerializer import ProductSerializer
from authApp.serializers.productSerializer import ProductSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductDetailView(views.APIView):


    def get(self,request,pk, format = None):
        
        queryset = Product.objects.get(pk)
        serializer_class = ProductSerializer(queryset)

        return response(serializer_class,status=status.HTTP_302_FOUND)


   
