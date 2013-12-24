from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from docutils.core import publish_parts

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def restructuredtext(value):
    return mark_safe(publish_parts(value, writer_name='html')['html_body'])
