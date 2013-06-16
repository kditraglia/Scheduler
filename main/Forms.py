from django import forms
from django.forms.widgets import Select, HiddenInput

class JQueryUIDatepickerWidget(forms.DateInput):
    def __init__(self, **kwargs):
        super(forms.DateInput, self).__init__(attrs={"class": "dateinput"}, **kwargs)
        
class JQueryUITimepickerWidget(forms.TimeInput):
    def __init__(self, **kwargs):
        super(forms.TimeInput, self).__init__(attrs={"class": "timeinput"}, **kwargs)

PROBLEMS = (('Problem', 'Problems'),('Sports/Work/Camp Physical', 'Physical'), ('Checkup', 'Checkup'))
valid_time_formats = ['%I:%M%p']

class AppointmentForm(forms.Form):
    firstName = forms.CharField(max_length=100, label='First Name:')
    lastName = forms.CharField(max_length=100, label='Last Name:')
    phoneNumber = forms.CharField(max_length=13, label='Phone Number:')
    dateScheduled = forms.DateField(widget=JQueryUIDatepickerWidget, label='Date:')
    timeScheduled = forms.TimeField(widget=JQueryUITimepickerWidget, label='Time:', input_formats=valid_time_formats)
    reason = forms.ChoiceField(widget=Select(attrs={"id": "select-choice-1"}), choices=PROBLEMS, label='Reason For Visit:')