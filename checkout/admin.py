from django.contrib import admin
from .models import Order, OrderBuyItem, OrderRentalItem

# Register your models here.


class OrderBuyItemAdminInline(admin.TabularInline):
    model = OrderBuyItem
    readonly_fields = ('buyitem_total',)


class OrderRentalItemAdminInline(admin.TabularInline):
    model = OrderRentalItem
    readonly_fields = ('rentalitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderBuyItemAdminInline, OrderRentalItemAdminInline)

    readonly_fields = ('order_number', 'order_date', 'grand_total',
                        'original_cart', 'original_cart_rental', 'stripe_pid'
                        )

    fields = ('order_number', 'user_profile', 'order_date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'grand_total',
              'original_cart', 'original_cart_rental', 'stripe_pid'
              )

    list_display = (
        'order_number', 'order_date', 'full_name', 'grand_total', 
        'delivery_date'
        )

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
