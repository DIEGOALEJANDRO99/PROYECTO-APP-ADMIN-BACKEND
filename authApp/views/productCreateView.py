from rest_framework import views, status
from rest_framework.response import Response
from authApp.serializers.productSerializer import ProductSerializer
from authApp.serializers.userSerializer import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ProductCreateView(views.APIView):

    def post(self,request,*args,**kwargs):
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(status=status.HTTP_201_CREATED)


