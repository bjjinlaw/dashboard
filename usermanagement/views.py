from usermanagement.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from usermanagement.serilaizers import UserRegisterSerializer
from rest_framework import status







class UserRegisterView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context={
               "message": "Created User Successfully !!",
               "status":status.HTTP_201_CREATED,
               "errors":[]
            }
            return Response(data=context)
        context={
                "message": "Unable To Create User !!",
                "status":status.HTTP_403_FORBIDDEN,
                "errors":serializer.errors
            }
        return Response(data=context)
        
        







