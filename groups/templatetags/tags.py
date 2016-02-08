import datetime
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def edit_list(object):
    url = reverse('admin:{0}_{1}_change'.format(object._meta.app_label.lower(), object._meta.object_name.lower()),
                  args=[object.id])
    return url