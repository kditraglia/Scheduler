from django.db import models
from django.db.models import permalink

class Appointment(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.SlugField(max_length=100, unique=True)
    dateScheduled = models.DateTimeField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return '%s %s' % self.firstName, self.lastName

#    @permalink
#    def get_absolute_url(self):
#        return ('view_blog_post', None, { 'slug': self.slug })
