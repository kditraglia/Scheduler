from django.db import models
from django.db.models import permalink

class Appointment(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=13)
    dateScheduled = models.DateTimeField()
    problem = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s %s' % (self.firstName, self.lastName)

