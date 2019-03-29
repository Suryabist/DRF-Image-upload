from django.shortcuts import render
from rest_framework import viewsets, parsers, decorators, response, status

from core.serializers import ProfileSerializer
from .models import Profile

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class =  ProfileSerializer
    #
    # @decorators.action(
    #     detail=True,
    #     methods=['PUT'],
    #     serializer_class=ProfilePicSerializer,
    #     parser_classes=[parsers.MultiPartParser],
    # )
    # def pic(self, request, pk):
    #     obj = self.get_object()
    #     serializer = self.serializer_class(obj, data=request.data,
    #                                        partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(serializer.data)
    #     return response.Response(serializer.errors,
    #                              status.HTTP_400_BAD_REQUEST)

