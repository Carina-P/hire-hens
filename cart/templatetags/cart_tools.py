from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Returns price times quantity.

    Input:
    price: float, price
    quantity: int, the number of items
    """
    return price * quantity


@register.filter(name='calc_cart_total')
def calc_cart_total(buy_total, rental_total):
    """
    Can be used to add to prices to get a total price.
    Returna buytotal + rental_total

    Input:
    buy_total: float, a price
    rent_total: float, a price
    """
    return buy_total + rental_total


@register.simple_tag(name='calc_rent_subtotal')
def calc_rent_subtotal(price, quantity, months):
    """
    Can be used to calculate a total price for a rental.
    Returns price * quantity * months

    Input:
    price: float, e.g. price per month
    quantity: number, e.g. number of items
    months: number, e.g. number of months
    """
    return price * quantity * int(months)
