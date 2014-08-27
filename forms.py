# -*- coding:utf-8 -*-
__author__ = 'tommy.yu'

from django.forms import ModelForm,Textarea
from models import  *
from django.forms.models import inlineformset_factory,modelform_factory

class todo_listForm(ModelForm):
    class Meta:
        model = todo_list
        # widgets = {
        #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }#yes,it works

# class todo_itemForm(ModelForm):
#     class Meta:
#         model = todo_item
#         exclude = ('list',)

todo_itemSet = inlineformset_factory(todo_list, todo_item, extra=1)
#modelform_factory()