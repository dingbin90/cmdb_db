from django import template

register = template.Library()

@register.simple_tag
def listtag(aseet):
    tag = []
    for i in aseet.tag.all():
        tag.append(i.name)
    print(tag)
    return ','.join(tag)
