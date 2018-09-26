from django import forms
from fortytwoapps.models import Contact
from datetime import date
from django.core.exceptions import ValidationError
from .widgets import Text, DateWidget


JABBER_ATTRS = {'pattern': '^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]'
                '{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$',
                'data-pattern-error': 'Enter a valid Jabber Id.',
                'class': 'form-control',
                'required': False}

EMAIL_ATTRS = {'pattern': '^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]'
               '{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$',
               'data-pattern-error': 'Enter a valid Email Id',
               'class': 'form-control',
               'required': False}


def validate_dob(value):
    today = date.today()
    max_age = date(today.year - 200, today.month, today.day)
    if value >= today or value < max_age:
        raise ValidationError(
            'Date greater than today and not older than 200 years'
        )


class UpdateContactForm(forms.ModelForm):

    class Meta:
        model = Contact

    name = forms.CharField(widget=Text(
                           attrs={'class': 'form-control', 'required': True,
                                  'data-required-error': 'Name is required.'
                                  }))
    lastname = forms.CharField(widget=Text(
                               attrs={'class': 'form-control',
                                      'required': True, 'data-required-error':
                                      'LastName is required.'}))
    dateofbirth = forms.DateField(widget=DateWidget(
                                  format='%Y-%m-%d',
                                  attrs={'class':
                                         'calendar-widget form-control',
                                         'required': True,
                                         'placeholder': 'yyyy-mm-dd',
                                         'data-dateofbirth':
                                         "dateofbirth"}),
                                  validators=[validate_dob])
    bio = forms.CharField(widget=forms.widgets.Textarea(
                          attrs={'class': 'form-control'}), required=False)
    email = forms.EmailField(widget=forms.widgets.EmailInput
                             (attrs=EMAIL_ATTRS), required=False)
    jabber = forms.CharField(widget=forms.widgets.TextInput
                             (attrs=JABBER_ATTRS), required=False)
    skype = forms.CharField(widget=Text(
                            attrs={'class': 'form-control'}), required=False)
    othercontacts = forms.CharField(widget=forms.widgets.Textarea(
                                    attrs={'class': 'form-control'}),
                                    required=False)
