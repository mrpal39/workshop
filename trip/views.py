from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import generics

from .models import Location
from .serializers import LocationSerializers
from rest_framework.response import Response
# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.csrf import csrf_exempt


class LocationView(generics.ListCreateAPIView):
    queryset=Location.objects.all()
    serializer_class=LocationSerializers



class LocationViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Location.objects.all()
    serializer_class=LocationSerializers


# class RoomImageView(generics.ListCreateAPIView):
#     queryset=RoomImage.objects.all()
#     serializer_class=RoomImageSerializers


@api_view(['GET','POST',"PUT","DELETE"])
@permission_classes({AllowAny})
@csrf_exempt
def locations_list(request):
    loc=Location.objects.all()
    serializer=LocationSerializers(loc)
    return Response(serializer)


def trip_home(request):
    return render(request,'trip.html')