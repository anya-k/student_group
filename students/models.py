from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models


class Student(models.Model):
    surname = models.CharField(max_length=40)
    first_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=40)
    number_card = models.PositiveIntegerField(
        unique=True,
        validators=[MinValueValidator(1000000000),
                    MaxValueValidator(9999999999)])
    date_of_birth = models.DateField()
    group = models.ForeignKey('groups.Group')

    def __unicode__(self):
        return '{0} {1}'.format(self.surname, self.first_name)

    def full_name(self):
        return '{0} {1} {2}'.format(self.surname, self.first_name, self.patronymic)

