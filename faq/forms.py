from django import forms
from .models import Faq


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['question', 'answer']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'question': 'Question',
            'answer': 'Answer',
        }

        self.fields['question'].widget.attrs['placeholder'] = f'{placeholders["question"]} *'
        self.fields['question'].widget.attrs['class'] = 'input-style'

        self.fields['answer'].widget.attrs['placeholder'] = f'{placeholders["answer"]} *'
        self.fields['answer'].widget.attrs['class'] = 'input-style'
