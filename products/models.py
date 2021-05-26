from django.db import models


class Category(models.Model):
    """
    Implements model Category that contains all products
    categories.
    """

    category = models.CharField(max_length=20)
    buyable = models.BooleanField()
    rentable = models.BooleanField()
    objects = models.Manager()

    def __str__(self):
        return self.category


class Product(models.Model):
    """
    Implements model Product that contains all products
    available
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=254)
    information = models.TextField()
    buying_price = models.DecimalField(max_digits=6, decimal_places=2)
    rental_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name
