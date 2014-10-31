__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

from api.models import Student, Company
from api.serializers import StudentSerializer, CompanySerializer

from django.http import HttpResponse
from django.core import mail
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def registration_submission(request):

        post = request.POST

        print post
        first_name = post.get('first_name')
        last_name = post.get('last_name')
        major = post.get('major')
        email = post.get('email')
        school = post.get('school')
        grade = post.get('grade')
        gender = post.get('gender')
        shirt = post.get('shirt')
        out_of_state = post.get('out_of_state')
        github = post.get('github')
        linkedin = post.get('linkedin')
        first = post.get('first')

        student = Student(first_name=first_name,
                          last_name=last_name,
                          major=major,
                          email=email,
                          school=school,
                          grade=grade,
                          gender=gender,
                          shirt_size=shirt,
                          out_of_state=out_of_state,
                          github_handle=github,
                          linkedin_link=linkedin,
                          first_hackathon=first)
        student.save()

        message = "%s %s has registered for MountainHacks 2015!" % (first_name, last_name)
        subject = "New Registrant!"
        connection = mail.get_connection()
        connection.open()
        complete_email = mail.EmailMessage(subject, message, email, ["mountainhacks@gmail.com"], connection=connection)
        complete_email.send()
        connection.close()

        return HttpResponse(status=200)