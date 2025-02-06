from django import forms
from .models import Message
from .models import LongTextSubmission

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'message']


class LongTextSubmissionForm(forms.ModelForm):
    class Meta:
        model = LongTextSubmission
        fields = ['text']
