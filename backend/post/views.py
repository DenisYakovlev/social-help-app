from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Post

# Create your views here.


class PostView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()