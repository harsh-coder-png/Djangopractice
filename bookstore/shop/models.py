from django.db import models

# Create your models here.
class Product(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=20)
    book_price = models.FloatField()
    book_image = models.ImageField(upload_to= 'images',default='')