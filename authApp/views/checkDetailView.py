from django.db.models import query
from rest_framework import generics, status, views
from authApp.models.check import Check
from authApp.serializers.checkSerializer import CheckSerializer
from django.http import response

class CheckDetailView(generics.RetrieveAPIView):

    queryset = Check.objects.all()
    serializer_class = CheckSerializer
    
    def get(self,request, *args,**kwargs):
    
        return super().get(request,*args,**kwargs)


   