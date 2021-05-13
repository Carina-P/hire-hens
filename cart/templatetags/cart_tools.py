from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name='calc_cart_total')
def calc_cart_total(buy_total, rental_total):
    return buy_total + rental_total


@register.simple_tag(name='calc_rent_subtotal')
def calc_rent_subtotal(price, quantity, months):
    return price * quantity * int(months)
