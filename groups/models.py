from __future__ import unicode_literals

from django.db import models
from students.models import Student


class Group(models.Model):
    name = models.CharField(max_length=20)
    headman = models.ForeignKey(Student, related_name='headman', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def amount_person(self):
        students = Student.objects.filter(group=self.id)
        return students.count()
