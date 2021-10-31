from django.db import models

# Create your models here.
from datetime import date


class Price(models.Model):
    period = models.DateField(auto_now=False, auto_now_add=False)
    rate = models.IntegerField()

    def __str__(self):
        return ("price")


class Hotel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(
        max_length=200, default="Start and end in San Francisco! With the in-depth cultural .")
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Rooms(models.Model):
    manager = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=5)
    room_type = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    price = models.FloatField(default=1000.00)
    no_of_days_advance = models.IntegerField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    room_image = models.ImageField(
        upload_to="media", height_field=None, width_field=None, max_length=None, default='0.jpeg')

    def __str__(self):
        return "Room No: "+str(self.id)


class RoomImage(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    room_image = models.ImageField(
        upload_to="media", height_field=None, width_field=None, max_length=None)


class Booking(models.Model):
    room_no = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    start_day = models.DateField(auto_now=False, auto_now_add=False)
    end_day = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.FloatField()
    booked_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Booking ID: "+str(self.id)

    @property
    def is_past_due(self):
        return date.today() & gt
        self.end_day
