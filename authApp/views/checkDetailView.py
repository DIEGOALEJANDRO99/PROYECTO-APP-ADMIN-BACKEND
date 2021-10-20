from rest_framework import status, views
from authApp.models.check import Check
from authApp.serializers.checkSerializer import CheckSerializer
from django.http import response

class CheckDetailView(views.APIView):
    
    def get(self,request,pk, format = None):
        
        queryset = Check.objects.get(pk)
        serializer_class = CheckSerializer(queryset)

        return response(serializer_class,status=status.HTTP_302_FOUND)


   