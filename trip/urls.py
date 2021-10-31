from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.trip_home,name="trip_home"),
    path('location/', views.LocationView.as_view(),name="trip_home"),

    path('location/<int:pk>/', views.LocationViewDetail.as_view(),name="trip"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
