"""
    DOC STRING
"""
# !/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from lists.models import Item


# class ItemForm(forms.Form):
#     """
#     DOC  DOC  DOC
#     """
#     item_text = forms.CharField(
#             widget=forms.fields.TextInput(attrs={
#                 'placeholder': 'Enter a to-do item',
#                 'class': 'form-control input-lg',
#         }),
#     )

EMPTY_ITEM_ERROR = "You can't have an empty list item"

class ItemForm(forms.models.ModelForm):
    """
    DOC  DOC  DOC
    """
    class Meta:
        model = Item
        fields = ('text', )
        widgets = {
                'text': forms.fields.TextInput(attrs={
                    'placeholder': 'Enter a to-do item',
                    'class' : 'form-control input-lg',
                }),
        }
        error_messages = {
                'text': {'required': "You can't have an empty list item"}
        }
    
    def save(self, for_list):
        self.instance.list = for_list
        return super().save()