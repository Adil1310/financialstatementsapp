from django import template

register = template.Library()

@register.filter
def format_number(value):
    try:
        value = float(value)
    except (ValueError, TypeError):
        return value

    formatted_number = "{:,.2f}".format(value).replace(",", "X").replace(".", ",").replace("X", " ")
    return formatted_number
