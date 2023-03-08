from django.db import models

class complaint(models.Model):
    name      = models.CharField(max_length=120)
    email     = models.EmailField(max_length=50)
    phone     = models.CharField(max_length=10)
    adhaar     = models.CharField(max_length=12)
    address    = models.CharField(max_length=100,default=True)
    description    = models.TextField()
    

    # def get_absolute_url(self):
    #     return f"/products/{self.id}"
class location(models.Model):
    latitude     = models.FloatField()
    longitude     = models.FloatField()
    
class witness(models.Model):
    name      = models.CharField(max_length=120)
    email     = models.EmailField(max_length=50)
    phone     = models.CharField(max_length=10)
    adhaar     = models.CharField(max_length=12)
    address    = models.CharField(max_length=100,default=True)
    crime_description    = models.TextField()

   


    