__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

from rest_framework import serializers

from api.models import Student, Company

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company