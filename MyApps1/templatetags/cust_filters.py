from django import template;
register=template.Library()
#@register.filter(name='fupper')
def ffu(value):
    result=value[:5].upper()
    return result
register.filter('fupper',ffu)