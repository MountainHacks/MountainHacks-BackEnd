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

    EXTRA_SMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'L'
    SHIRT_SIZES = (
        (EXTRA_SMALL, 'Extra Small'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (EXTRA_LARGE, 'Extra Large'),
    )

    MALE = 'M'
    FEMALE = 'F'
    GENDERS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    HIGH_SCHOOL = 'HS'
    GRAD_STUDENT = 'GS'
    GRADES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (HIGH_SCHOOL, 'High School'),
        (GRAD_STUDENT, 'Graduate Student')
    )

    first_name = models.CharField('First Name', max_length=75)
    last_name = models.CharField('Last Name', max_length=100)
    major = models.CharField('Major', max_length=50)
    gender = models.CharField('Gender', max_length=1, choices=GENDERS)
    email = models.EmailField('Email', max_length=175)
    school = models.CharField('School', max_length=200)
    grade = models.CharField('Grade', max_length=75, choices=GRADES)
    first_hackathon = models.BooleanField('First Hackathon')
    github_handle = models.CharField('Github Handle', max_length=50)
    linkedin_link = models.URLField('LinkedIn Link')
    shirt_size = models.CharField('Shirt Size', max_length=3, choices=SHIRT_SIZES)
    out_of_state = models.BooleanField('Out-of-State')

class Company(models.Model):

    name = models.CharField('Company Name', max_length=100)
    city = models.CharField('City', max_length=150)
    state = USStateField('State')
    phone_number = PhoneNumberField('Phone Number')
    contact_email = models.EmailField('Contact Email', max_length=150)
    contact_name = models.CharField('Contact Name', max_length=150)


