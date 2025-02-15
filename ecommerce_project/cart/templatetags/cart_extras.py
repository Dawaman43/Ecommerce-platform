
from django import template

register = template.Library()

@register.filter(name='mul')
def mul(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return value
