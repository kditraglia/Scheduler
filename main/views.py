from main.models import Appointment
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):

    if request.method == 'POST':
        appointment = Appointment(
           firstName=request.POST['First'],
           lastName=request.POST['Last'],
           dateScheduled=request.POST['Date'],
           problem=request.POST['problem'],)
        appointment.save()

    return render_to_response('index.html', {
        'appointments': Appointment.objects.all(),
    }, context_instance=RequestContext(request))
