# -*- coding:utf-8 -*-
__author__ = 'tommy.yu'

from django.forms import ModelForm
from models import  *
from django.forms.models import inlineformset_factory

class todo_listForm(ModelForm):
    class Meta:
        model = todo_list

# class todo_itemForm(ModelForm):
#     class Meta:
#         model = todo_item
#         exclude = ('list',)

todo_itemSet = inlineformset_factory(todo_list, todo_item, extra=1)