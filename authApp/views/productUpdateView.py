
from rest_framework import views, status
from rest_framework.response import Response
from authApp.models.product import Product
from authApp.serializers.productSerializer import ProductSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ProductUpdateView(views.APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def put(self, request, pk):

        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
