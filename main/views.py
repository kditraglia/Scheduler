from main.models import Appointment, Problem
from main.Forms import AppointmentForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 
from datetime import time, timedelta, date, datetime
import calendar

def index(request):
    return render_to_response('index.html', { }, context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', { }, context_instance=RequestContext(request))

def directions(request):
    return render_to_response('directions.html', { }, context_instance=RequestContext(request))

def view(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        appointments = Appointment.objects.filter(firstName__icontains=q)
        return render_to_response('view.html',
            {'appointments': appointments, 'query': q},
            context_instance=RequestContext(request))
    return render_to_response('view.html',{},context_instance=RequestContext(request))

def show_appointment(request, slug):
    appointment = get_object_or_404(Appointment, firstName=slug)
    return render_to_response('show_appointment.html', {
        'appointment': appointment,
    }, context_instance=RequestContext(request))

def appointment(request):
    problems = []
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            appointment = Appointment(
               firstName=cd['firstName'],
               lastName=cd['lastName'],
               phoneNumber=cd['phoneNumber'],
               dateScheduled=cd['dateScheduled'],
               problem=cd['reason'],)
            appointment.save()       
            return render_to_response('show_appointment.html', {
                'appointment': appointment,
            }, context_instance=RequestContext(request))
    else:
        form = AppointmentForm()
        problems = Problem.objects.all()
    return render_to_response('appointment.html', {
        'form': form,
        'problems': problems,
    }, context_instance=RequestContext(request))
