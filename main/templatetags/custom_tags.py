from django import template
import datetime

register = template.Library()


@register.simple_tag
def mediapath_tag(path):
    if path:
        return f'/media/{path}'
    return '#'


@register.filter()
def mediapath(path):
    if path:
        return f'/media/{path}'
    return '#'


@register.simple_tag
def this_year(format_string):
    return datetime.datetime.now().strftime(format_string)
