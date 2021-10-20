 
from rest_framework import response, views, status

from authApp.models.product import Product


class ProductDeleteView(views.APIView):

       def delete(self, request, pk, format=None):

              queryset = Product.objects.get_object(pk)
              queryset.delete()
              return response(status=status.HTTP_204_NO_CONTENT)