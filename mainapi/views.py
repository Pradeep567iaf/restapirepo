
from django.shortcuts import render
from rest_framework import status
from .models import student
from .serializers import StudentSerializer

from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

class StudentViewSet(ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BaseAuthentication]
    # permission_classes = [IsAuthenticated]


# class StudentViewSet(viewsets.ViewSet):
#     # authentication_classes = [BaseAuthentication]
#     # permission_classes = [IsAuthenticated]
#     def list(self,request):
#         stu = student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)
#     def retrieve(self,request,pk=None):
#         id = pk
#         stu = student.objects.get(pk=id)
#         serializer = StudentSerializer(stu)
#         return Response(serializer.data)
#     def create(self,request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":'student created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self,request,pk):
#         id = pk
#         stu = student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Student updated completely'})
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
       
#     def partial_update(self,request,pk):
#         id = pk
#         stu = student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'student updated partially'})
#         return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
#     def destroy(self,request,pk):
#         id = pk
#         stu = student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Student deleted successfully'})    
        
