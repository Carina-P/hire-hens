import uuid
from django.db import models
from django.db.models import Sum

from products.models import Product

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    delivery_date = models.DateTimeField(null=True, blank=True)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        buy_total = self.buyitems.aggregate(
            Sum('buyitem_total')
            )['buyitem_total__sum'] or 0

        rent_total = self.rentalitems.aggregate(
            Sum('rentalitem_total')
            )['rentalitem_total__sum'] or 0

        self.grand_total = buy_total + rent_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderBuyItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='buyitems'
        )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
        )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    buyitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
        )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the buyitem total
        and update the order total.
        """
        self.buyitem_total = self.product.buying_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name


class OrderRentalItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='rentalitems'
        )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
        )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    months = models.IntegerField(null=False, blank=False, default=0)
    rentalitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
        )
    end_of_rental = (models.DateTimeField(null=True, blank=True))

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the rentalitem total
        and update the order total.
        """
        self.rentalitem_total = self.product.rental_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name
