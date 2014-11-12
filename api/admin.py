__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

from django.contrib import admin
from api.models import Student, Company

# Register your models here.
admin.site.register(Student)
admin.site.register(Company)
