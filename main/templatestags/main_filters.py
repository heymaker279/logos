from django import template

register = template.Library()


@register.filter
def get_count(value, start_index=0):
    return range(start_index, value + start_index)
