from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from credit.serializers import RequestSerializer


class MakeRequestView(generics.CreateAPIView):
    serializer_class = RequestSerializer
