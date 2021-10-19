from django.conf import settings
from django.http.response import ResponseHeaders
from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class =UserSerializer

    def get(self,request,*args,**kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        Valid_data = token_backend.decode(token ,verify=False)
        
        if Valid_data['user_id'] != kwargs['pk']:
            invalid_response ={
                'detail': 'Unauthorized'
            }
        
            return Response(invalid_response,status=status.HTTP_401_UNAUTHORIZED)


        return super().get(request,*args,**kwargs)

