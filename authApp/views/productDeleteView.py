 
from django.http.response import Http404
from rest_framework import  views, status
from authApp.models.product import Product
from rest_framework.response import Response

class ProductDeleteView(views.APIView):


       def get_object(self, pk):
              try:
                     return Product.objects.get(pk=pk)
              except Product.DoesNotExist:
                     raise Http404



       def delete(self,request,pk,*args,**kwargs):

              product = self.get_object(pk)
              product.delete()

              return Response(status=status.HTTP_202_ACCEPTED)