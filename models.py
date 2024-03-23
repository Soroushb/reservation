from django.db import models

# Create your models here.
# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.FloatField(null=False) 
   inventory = models.IntegerField(max_length=5)

   def __str__(self):
      return self.name
   
class Booking(models.Model):
   name = models.CharField(max_length = 255)
   no_of_guests = models.IntegerField(6)
   bookingDate = models.DateTimeField