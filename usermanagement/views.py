from usermanagement.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from usermanagement.serilaizers import UserRegisterSerializer,UserDetailUpdataSerializer
from rest_framework import status
from rest_framework.permissions import IsAdminUser




class UserRegisterView(APIView):
    serializer=UserRegisterSerializer
    permission_classes=[IsAdminUser]
    
    def post(self,request,*args,**kwargs):
        serializer=self.serializer(data=request.data)
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
                "errors":serializer.errors,
                "data":serializer.data
            }
        return Response(data=context)
    
    


class UserDetailUpdateDeleteView(APIView):
    serializer=UserDetailUpdataSerializer

    def get_object(self):
        user=User.objects.filter(pk=self.kwargs.get("pk")).first()
        return user
    

    def put(self,request,*args,**kwargs):   
        user=self.get_object()
        if not user:
            context={
               "message": "No User Found !!",
               "status":status.HTTP_400_BAD_REQUEST,
               "errors":[],
            }
            return Response(data=context)
            
            
        serializer=self.serializer(user,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            context={
               "message": "Updated Succesffully  !!",
               "status":status.HTTP_201_CREATED,
               "errors":[],
               "data":serializer.data
            }
            return Response(data=context)
        
        context={
            "message": "Unable To Update User!!",
            "status":status.HTTP_403_FORBIDDEN,
            "errors":serializer.errors,
        }
        return Response(data=context)
    
    
    
    def delete(self,request,*args,**kwargs):
        user=self.get_object()
        if not user:
            context={
               "message": "No User Found !!",
               "status":status.HTTP_400_BAD_REQUEST,
               "errors":[],
            }
            return Response(data=context)
        
        user.delete()
        context={
            "message": "Deleted !!!",
            "status":status.HTTP_404_NOT_FOUND,
            "errors":[]
        }
        return Response(context)
        
        
        







