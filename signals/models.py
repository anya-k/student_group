from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from students.models import Student
from groups.models import Group

EVENT_CHOICES = (
    ('C', 'create'),
    ('E', 'edit'),
    ('D', 'delete'),
    )


class Signal(models.Model):
    event = models.CharField(choices=EVENT_CHOICES, max_length=1)
    name_model = models.CharField(max_length=30)
    name_object = models.CharField(max_length=100)
    date_time = models.DateTimeField()

    def __unicode__(self):
        return self.name_object


def save_arguments(p, instance, **kwargs):
    p.name_model = kwargs.get('sender', 'Unknown')
    p.name_object = instance
    p.date_time = timezone.now()
    p.save()


@receiver(post_save, sender=Student)
@receiver(post_save, sender=Group)
def save_object(instance, **kwargs):
    p = Signal()
    if kwargs.get('created', False):
        p.event = EVENT_CHOICES[0][0]
    else:
        p.event = EVENT_CHOICES[1][0]
    save_arguments(p, instance, **kwargs)


@receiver(post_delete, sender=Student)
@receiver(post_delete, sender=Group)
def delete_object(instance, **kwargs):
    p = Signal()
    p.event = EVENT_CHOICES[2][0]
    save_arguments(p, instance, **kwargs)