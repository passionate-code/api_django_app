import datetime
from django import template

register = template.Library()

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter
def timestamp_to_date(timestamp):
    try:
        date_str = timestamp.strftime("%d/%m/%Y")
    except AttributeError:
        date_str = None
    return date_str

