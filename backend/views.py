from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status, generics
from .serializers import UserSerializer, ActivityLogSerializer, WorkoutSerializer, GoalSerializer, StatSheetSerializer
from .models import User, ActivityLog, Workout, Goal, StatSheet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.exceptions import ValidationError

# Create your views here.
class UserView(APIView):
    serialzier_class = UserSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, format=None):
        userId = request.GET.get(self.lookup_url_kwarg)
        if userId:
            user = User.objects.filter(id=userId)
            if len(user) > 0:
                data = UserSerializer(user[0]).data
                return Response(data, status=status.HTTP_200_OK)
            return Response({'User Not Found': 'Invalid User ID.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': 'User ID not found in request.'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        """ if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create() """
        
        serializer = self.serialzier_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"Bad Request": "User could not be created with given entries."}, status=status.HTTP_400_BAD_REQUEST)
        

class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

