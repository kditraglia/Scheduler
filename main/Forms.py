from django import forms
from django.forms.widgets import Select, HiddenInput

class JQueryUIDatepickerWidget(forms.DateInput):
    def __init__(self, **kwargs):
        super(forms.DateInput, self).__init__(attrs={"class": "dateinput"}, **kwargs)
        
class JQueryUITimepickerWidget(forms.TimeInput):
    def __init__(self, **kwargs):
        super(forms.TimeInput, self).__init__(attrs={"class": "timeinput"}, **kwargs)

PROBLEMS = (('Problem', 'Problems'),('Sports/Work/Camp Physical', 'Physical'), ('Checkup', 'Checkup'))
#hack
TIMES = ('8:00', '8:15', '8:30', '8:45', '9:00')

class AppointmentForm(forms.Form):
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    phoneNumber = forms.CharField(max_length=13)
    dateScheduled = forms.DateField(widget=JQueryUIDatepickerWidget)
    timeScheduled = forms.TimeField(widget=JQueryUITimepickerWidget)
    ReasonForAppointment = forms.ChoiceField(widget=Select(attrs={"id": "select-choice-1"}), choices=PROBLEMS)