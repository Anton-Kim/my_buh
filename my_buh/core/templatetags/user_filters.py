from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


# @register.filter
# def divide(value, n):
#     try:
#         return int(value) / int(n)
#     except (ValueError, ZeroDivisionError):
#         return None


@register.filter
def balance_percentage(count, sold_count):
    try:
        return int(100 / (count + sold_count) * count)
    except (ValueError, ZeroDivisionError):
        return None


# @register.filter
# def benefit(earnings, sold_count, purchase_unit_price):
#     try:
#         return earnings - sold_count * purchase_unit_price
#     except (ValueError, ZeroDivisionError):
#         return None


@register.simple_tag
def multiple_args_tag(earnings, sold_count, purchase_unit_price):
    try:
        return int(earnings) - int(sold_count) * int(purchase_unit_price)
    except (ValueError, ZeroDivisionError):
        return None
