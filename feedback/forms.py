from django import forms
from django.forms import ModelForm
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """
    Create a form for the contact model
    """
    class Meta:
        """
        Display the required fields
        """
        model = Feedback
        fields = "__all__"

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        """
        Add Placeholder to form fields
        """
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'phone': 'Phone number',
            'message': 'Your Message',
        }

        for field in self.fields:
            if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
            else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            
            # add class to fields
            self.fields[field].widget.attrs['class'] = 'my-2'