__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
    url(r'^students$', views.StudentListView.as_view(), name='student_list'),
    url(r'^companies$', views.CompanyListView.as_view(), name='company_list'),
    url(r'^companies/(?P<pk>[0-9]+)$', views.CompanyInstanceView.as_view(), name='company_instance'),
    url(r'submit', views.registration_submission, name='registration_submission'),
    url(r'token', views.get_token, name='token'),
)
