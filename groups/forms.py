# -*- coding: utf-8 -*-
from django import forms

from groups.models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        labels = {'name': "Название",
                  }
        fields = ["name",]

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': 'Поле {fieldname} обязательно должно быть заполнено!'.format(
                fieldname=field.label)}


class GroupUpdateForm(forms.ModelForm):
    class Meta:
        model = Group
        labels = {'name': "Название",
                  'headman': "Староста",
                  }
        fields = ["name","headman"]

    def __init__(self, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': 'Поле {fieldname} обязательно должно быть заполнено!'.format(
                fieldname=field.label)}
