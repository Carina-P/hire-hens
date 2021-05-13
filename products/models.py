from django.db import models

# Create your models here.


class Category(models.Model):

    category = models.CharField(max_length=20)
    buyable = models.BooleanField()
    rentable = models.BooleanField()

    def __str__(self):
        return self.category


class Product(models.Model):
#    category = models.ForeignKey(
#        'Category', null=True, blank=True, on_delete=models.SET_NULL
#        )
    name = models.CharField(max_length=254)
    information = models.TextField()
    buying_price = models.DecimalField(max_digits=6, decimal_places=2)
    rental_price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
