from django.contrib import admin
from .models import car_brand
# Register your models here.

class brands_slug(admin.ModelAdmin):
    prepopulated_fields = {'slug':('brand_name',)}
    list_display = ['brand_name', 'slug']

admin.site.register(car_brand,brands_slug)