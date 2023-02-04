from django import template
register=template.Library()
@register.filter(name='c_and_c')
def cut_and_concat(value,args):
    result=value[:5]+str(args);
    return result