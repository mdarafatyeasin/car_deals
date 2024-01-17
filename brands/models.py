from django.db import models

# Create your models here.
class car_brand (models.Model):
    brand_name = models.CharField(max_length = 100, null=True, blank=True)

    def __str__ (self):
        return self.brand_name