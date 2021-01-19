from django import forms

from .models import Bb


class BbForm(forms.ModelForm):
    """Форма для ввода новых объявлений"""

    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
