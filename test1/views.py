# test1/views.py

from rest_framework import viewsets
from .models import Project
from django.contrib.auth.models import User
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
