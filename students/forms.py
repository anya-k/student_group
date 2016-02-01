# -*- coding: utf-8 -*-
from django import forms

from students.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        labels = {'first_name': "Имя",
                  'surname': "Фамилия",
                  'patronymic': "Отчество",
                  'date_of_birth': "Дата рождения",
                  'number_card': "Номер студенческого билета",
                  'group': "Группа",
                  }
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': 'Поле {fieldname} обязательно должно быть заполнено!'.format(
                fieldname=field.label)}
