from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderBuyItem, OrderRentalItem


@receiver(post_save, sender=OrderBuyItem)
def update_on_buyitem_save(sender, instance, created, **kwargs):
    """
    Update order total on buyitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderBuyItem)
def update_on_buyitem_delete(sender, instance, **kwargs):
    """
    Update order total on buyitem delete
    """
    instance.order.update_total()


@receiver(post_save, sender=OrderRentalItem)
def update_on_rentalitem_save(sender, instance, created, **kwargs):
    """
    Update order total on rentalitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderRentalItem)
def update_on_rentalitem_delete(sender, instance, **kwargs):
    """
    Update order total on rentalitem delete
    """
    instance.order.update_total()
