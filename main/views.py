from main.models import Appointment
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 
from datetime import time, timedelta, date, datetime
import calendar

def index(request):
    list = []
    for x in range(0, 37):
        dt = datetime.combine(date.today(), time(8, 0)) + timedelta(minutes=15*x)
        list.append(dt.time().strftime('%I:%M %p'))
    if request.method == 'POST':
        appointment = Appointment(
           firstName=request.POST['First'],
           lastName=request.POST['Last'],
           dateScheduled=request.POST['Date'],
           problem=request.POST['problem'],)
        appointment.save()
        return HttpResponseRedirect(reverse("main.views.index"))
    return render_to_response('index.html', {
        'appointments': Appointment.objects.all(),
        'times': list,
    }, context_instance=RequestContext(request))

def about(request):

    return render_to_response('about.html', {
	  }, context_instance=RequestContext(request))

def directions(request):

    return render_to_response('directions.html', {
	  }, context_instance=RequestContext(request))

def appointment(request):

    return render_to_response('appointment.html', {
	  }, context_instance=RequestContext(request))
