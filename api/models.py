__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

from django.db import models
from localflavor.us.models import USStateField, PhoneNumberField

# needed for South to cooperate with localflavor fields
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^localflavor\.us\.models\.USStateField"])
add_introspection_rules([], ["^localflavor\.us\.models\.PhoneNumberField"])

class SessionToken(models.Model):

    val = models.CharField('Value', max_length=100)

class Student(models.Model):

    first_name = models.CharField('First Name', max_length=75)
    last_name = models.CharField('Last Name', max_length=100)
    major = models.CharField('Major', blank=True, max_length=50)
    gender = models.CharField('Gender', blank=True, max_length=1)
    email = models.EmailField('Email', max_length=175)
    school = models.CharField('School', max_length=200)
    grade = models.CharField('Grade', max_length=75)
    first_hackathon = models.BooleanField('First Hackathon')
    github_handle = models.CharField('Github Handle', max_length=50, blank=True, null=True)
    linkedin_link = models.URLField('LinkedIn Link', blank=True, null=True)
    shirt_size = models.CharField('Shirt Size', max_length=3)
    out_of_state = models.BooleanField('Out-of-State')
    resume = models.FileField(upload_to='resumes/', null=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['id']

    def __unicode__(self):
        return '%s %s -- %s' % (self.first_name, self.last_name, self.school)

class Company(models.Model):

    name = models.CharField('Company Name', max_length=100)
    city = models.CharField('City', max_length=150)
    state = USStateField('State')
    phone_number = PhoneNumberField('Phone Number')
    contact_email = models.EmailField('Contact Email', max_length=150)
    contact_name = models.CharField('Contact Name', max_length=150)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['id']

    def __unicode__(self):
        return self.name


