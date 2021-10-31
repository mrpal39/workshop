from django.core import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.core import serializers
from django.db.models import fields
from rest_framework import serializers
from urllib import request
from rest_framework import routers, serializers, viewsets
from django.http import HttpResponse
from rest_framework import serializers

from .models import Location


class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields="__all__"



        
