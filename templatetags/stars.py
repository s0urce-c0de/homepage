from django.templatetags.static import static
from django import template
from django.utils.safestring import mark_safe
from math import floor, ceil

register = template.Library()

@register.simple_tag
def stars(stars, outof):
  return ''

@register.simple_tag
def load_star_css():
  return mark_safe(f'<link rel="stylesheet" href="{static("stars.css")}">')