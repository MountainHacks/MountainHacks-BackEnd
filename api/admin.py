__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

from django.contrib import admin
from api.models import Student

# Register your models here.
admin.site.register(Student)
