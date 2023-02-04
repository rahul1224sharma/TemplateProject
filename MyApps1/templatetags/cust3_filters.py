from django import template
register=template.Library()
@register.filter(name='truncate')
def truncate(value):
    result=value[0:5]
    return result