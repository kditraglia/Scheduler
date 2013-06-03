from django import forms
from django.forms.widgets import Select, HiddenInput

class JQueryUIDatepickerWidget(forms.DateInput):
    def __init__(self, **kwargs):
        super(forms.DateInput, self).__init__(attrs={"class": "dateinput"}, **kwargs)

PROBLEMS = (('Sick', 'Sick'),('Sports Physical', 'Sports Physical'))

class AppointmentForm(forms.Form):
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    phoneNumber = forms.CharField(max_length=13)
    dateScheduled = forms.DateField(widget=JQueryUIDatepickerWidget)
    problem = forms.ChoiceField(widget=Select(attrs={"id": "select-choice-1"}), choices=PROBLEMS)