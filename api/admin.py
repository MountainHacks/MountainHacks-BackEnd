__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

from django.contrib import admin
from api.models import Student, Company#, SessionToken

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('registration_date', 'is_confirmed')
    exclude = ('confirmation_code',)
    list_filter = ('is_confirmed', 'gender', 'school', 'grade', 'shirt_size', 'out_of_state')

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Company)
#admin.site.register(SessionToken)
