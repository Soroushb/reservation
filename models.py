from django.db import models

# Create your models here.
# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.FloatField(null=False) 
   inventory = models.IntegerField(max_length=5)

   def __str__(self):
      return self.name
   
class MenuItem(models.Model):
   title = models.CharField(max_length=255)
   price = models.DecimalField(max_digits=6, decimal_places=2)
   inventory = models.SmallIntegerField()

   def get_item(self):
      return f'{self.title} : {str(self.price)}'
   
class Booking(models.Model):
   name = models.CharField(max_length = 255)
   no_of_guests = models.IntegerField(6)
   bookingDate = models.DateTimeField