from django.db import models

class MeetingPoint(models.Model):
    # define fields
    name = models.CharField(max_length=100)
    # define a method to return the name of the meeting point
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

# create a model for RideType
class RideType(models.Model):
    # define fields
    name = models.CharField(max_length=255)
    # define a method to return the name of the ride type
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Rider(models.Model):
    # define fields
    name = models.CharField(max_length=100)
    # define a method to return the name of the rider
    def __str__(self):
        return self.name
    
    # sort by name
    class Meta:
        ordering = ['name']
    
class Ride(models.Model):
    # define fields
    name = models.CharField(max_length=255)
    comments = models.TextField()
    start_date = models.DateTimeField("start date")
    meeting_point = models.ForeignKey(MeetingPoint, on_delete=models.CASCADE)
    distance = models.CharField(max_length=255)
    speed = models.CharField(max_length=255)
    ride_type = models.ForeignKey(RideType, on_delete=models.CASCADE)
    route = models.URLField()
    cafe_stop = models.CharField(max_length=255)
    # rider = models.ManyToManyField(Rider)
    
    route.blank = True

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("ride_manager:show_ride", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ['-start_date']