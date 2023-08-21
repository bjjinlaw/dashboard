from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userprofile.models import AdminProfile, TeacherProfile, StudentProfile
from userprofile.serializers import AdminProfileSerializer, StudentProfileSerializer, TeacherProfileSerializer



class TeacherProfileRegisterView(APIView):
    serializer=TeacherProfileSerializer
    permission_classes=[]
    # authentication_classes=[]
    
    def post(self,request,*args,**kwargs):
        serializer=self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context={
               "message": "Created Teacher Profile Successfully !!",
               "status":status.HTTP_201_CREATED,
               "errors":[],
               "data":serializer.data,
            }
            return Response(data=context)
        context={
                "message": "Unable To Create Teacher Profile !!",
                "status":status.HTTP_400_BAD_REQUEST,
                "errors":serializer.errors,
                "data":[]
            }
        return Response(data=context)
    
    
class TeacherProfileUpdateView(APIView):
    serializer_class = TeacherProfileSerializer

    def put(self, request, *args, **kwargs):
        profile = TeacherProfile.objects.get(pk=self.kwargs.get("pk"))
        serializer = self.serializer_class(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "message": "Updated Teacher Profile Successfully !!",
                "status": status.HTTP_200_OK,
                "errors": [],
                "data": serializer.data
            }
            return Response(data=context)
        context = {
            "message": "Unable To Update Teacher Profile !!",
            "status": status.HTTP_400_BAD_REQUEST,
            "errors": serializer.errors,
        }
        return Response(data=context)
    
    
class TeacherProfileDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        profile = TeacherProfile.objects.get(pk=self.kwargs.get("pk"))
        profile.delete()
        context = {
            "message": "Deleted Teacher Profile !!",
            "status": status.HTTP_204_NO_CONTENT,
            "errors": [],
        }
        return Response(context)




class StudentProfileRegisterView(APIView):
    serializer=StudentProfileSerializer
    permission_classes=[]
    # authentication_classes=[]
    
    def post(self,request,*args,**kwargs):
        serializer=self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context={
               "message": "Created Student Profile Successfully !!",
               "status":status.HTTP_201_CREATED,
               "errors":[],
               "data":serializer.data,
            }
            return Response(data=context)
        context={
                "message": "Unable To Create Student Profile !!",
                "status":status.HTTP_400_BAD_REQUEST,
                "errors":serializer.errors,
                "data":[]
            }
        return Response(data=context)
    
    
class StudentProfileUpdateView(APIView):
    serializer_class = StudentProfileSerializer

    def put(self, request, *args, **kwargs):
        profile = StudentProfile.objects.get(pk=self.kwargs.get("pk"))
        serializer = self.serializer_class(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "message": "Updated Student Profile Successfully !!",
                "status": status.HTTP_200_OK,
                "errors": [],
                "data": serializer.data
            }
            return Response(data=context)
        context = {
            "message": "Unable To Update Student Profile !!",
            "status": status.HTTP_400_BAD_REQUEST,
            "errors": serializer.errors,
        }
        return Response(data=context)
    
    
class StudentProfileDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        profile = StudentProfile.objects.get(pk=self.kwargs.get("pk"))
        profile.delete()
        context = {
            "message": "Deleted Student Profile !!",
            "status": status.HTTP_204_NO_CONTENT,
            "errors": [],
        }
        return Response(context)





class AdminProfileRegisterView(APIView):
    serializer=AdminProfileSerializer
    permission_classes=[]
    # authentication_classes=[]
    
    def post(self,request,*args,**kwargs):
        serializer=self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context={
               "message": "Created Admin Profile Successfully !!",
               "status":status.HTTP_201_CREATED,
               "errors":[],
               "data":serializer.data,
            }
            return Response(data=context)
        context={
                "message": "Unable To Create Admin Profile !!",
                "status":status.HTTP_400_BAD_REQUEST,
                "errors":serializer.errors,
                "data":[]
            }
        return Response(data=context)
    
    
class AdminProfileUpdateView(APIView):
    serializer_class = AdminProfileSerializer

    def put(self, request, *args, **kwargs):
        profile = AdminProfile.objects.get(pk=self.kwargs.get("pk"))
        serializer = self.serializer_class(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "message": "Updated Admin Profile Successfully !!",
                "status": status.HTTP_200_OK,
                "errors": [],
                "data": serializer.data
            }
            return Response(data=context)
        context = {
            "message": "Unable To Update Admin Profile !!",
            "status": status.HTTP_400_BAD_REQUEST,
            "errors": serializer.errors,
        }
        return Response(data=context)
    
    
class AdminProfileDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        profile = AdminProfile.objects.get(pk=self.kwargs.get("pk"))
        profile.delete()
        context = {
            "message": "Deleted Admin Profile !!",
            "status": status.HTTP_204_NO_CONTENT,
            "errors": [],
        }
        return Response(context)
