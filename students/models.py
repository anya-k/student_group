from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    surname = models.CharField(max_length=40)
    first_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=40)
    number_card = models.IntegerField(unique=True)
    date_of_birth = models.DateField()
    group = models.ForeignKey('Group')

    def __unicode__(self):
        return '{0} {1}'.format(self.surname, self.first_name)


class Group(models.Model):
    name = models.CharField(max_length=20)
    headman = models.ForeignKey(Student)

    def __unicode__(self):
        return self.name
