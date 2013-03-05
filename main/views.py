from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
    return render_to_response('index.html', {
        'appointments': Appointment.objects.all(),
    }, context_instance=RequestContext(request))
