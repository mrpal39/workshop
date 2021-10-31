from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/', views.api_root),
    path('hotel/', views.HotelList.as_view()),
    path('hotel/<int:pk>/', views.HotelDetail.as_view()),
    path('hotels/room/<int:pk>', views.Roomlist.as_view()),
    path('hotel/<int:pk>/room/', views.RoomDetail.as_view()),
    path('', views.hotelpage,name='hotel_page'),


    path('room/', views.RoomImageView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
