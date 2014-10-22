__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

from api.models import Student, Company
from api.serializers import StudentSerializer, CompanySerializer

from rest_framework import generics

class StudentListView(generics.ListCreateAPIView):
    """ Returns a list of serialized Student objects in JSON format.
    Allows:
        GET
        POST
    """

    model = Student
    serializer_class = StudentSerializer


class StudentInstanceView(generics.RetrieveUpdateDestroyAPIView):
    """ Returns a single serialized Student object in JSON format.
    Allows:
        GET
        PUT
        PATCH
        DELETE
    """

    model = Student
    serializer_class = StudentSerializer


class CompanyListView(generics.ListCreateAPIView):
    """ Returns a list of serialized Company objects in JSON format.
    Allows:
        GET
        POST
    """

    model = Company
    serializer_class = CompanySerializer


class CompanyInstanceView(generics.RetrieveUpdateDestroyAPIView):
    """ Returns a single serialized Company object in JSON format.
    Allows:
        GET
        PUT
        PATCH
        DELETE
    """

    model = Company
    serializer_class = CompanySerializer