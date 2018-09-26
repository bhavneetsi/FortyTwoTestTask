from django import forms


class Text(forms.TextInput):

    def __init__(self, format=None, attrs=None):
        super(Text, self).__init__(attrs=attrs)


class DateWidget(forms.DateInput):

    class Media:
        js = ('js/date_widget.js',)

    def __init__(self, format=None, attrs=None):
        if format is None:
            format = '%Y-%m-%d'

        super(DateWidget, self).__init__(format=format, attrs=attrs)
