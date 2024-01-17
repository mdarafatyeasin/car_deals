from django.db import models
from brands.models import car_brand

# Create your models here.
class car(models.Model):
    name = models.CharField(max_length = 100)
    brand_name = models.ForeignKey(car_brand, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.CharField(max_length = 10)
    quantity = models.CharField(max_length = 10)
    picture = models.ImageField(upload_to="cars/media/upload", null=True, blank=True)

    def __str__(self):
        return self.name