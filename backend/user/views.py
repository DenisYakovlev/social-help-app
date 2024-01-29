from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .models import AnonUser

# Create your views here.


class UserAuth(APIView):
    permission_classes = []

    @transaction.atomic
    def post(self, request):
        new_user = AnonUser()
        new_user.save()

        token, created = Token.objects.get_or_create(user=new_user)
        return Response({'token': token.key}, status.HTTP_201_CREATED)
        