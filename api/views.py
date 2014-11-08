__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

from api.models import Student, Company, SessionToken
from api.serializers import StudentSerializer, CompanySerializer

from django.http import HttpResponse
from django.core import mail
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from api.tokens import TokenGenerator
from rest_framework.exceptions import PermissionDenied

class StudentListView(generics.ListCreateAPIView):
    """ Returns a list of serialized Student objects in JSON format.
    Allows:
        GET
        POST
    """

    model = Student
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_X_MOUNTAINHACKS')
        if not token:
            print "no token"
            raise PermissionDenied({"message":"You don't have permission to access"})
        try:
            tokobj = SessionToken.objects.get(val=token)
            tokobj.delete()
            return super(StudentListView, self).get(request, *args, **kwargs)
        except SessionToken.DoesNotExist:
            print "token does not exist"
            raise PermissionDenied({"message":"You don't have permission to access"})


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

    def get(self, request, *args, **kwargs):
        for k,v in request.META.iteritems():
            print str(k) + "           " + str(v)
        token = request.META.get('HTTP_X_MOUNTAINHACKS')
        if not token:
            print "no token"
            raise PermissionDenied({"message":"You don't have permission to access"})
        try:
            tokobj = SessionToken.objects.get(val=token)
            tokobj.delete()
            return super(StudentInstanceView, self).get(request, *args, **kwargs)
        except SessionToken.DoesNotExist:
            print "token does not exist"
            raise PermissionDenied({"message":"You don't have permission to access"})


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

def get_token(request):
    return HttpResponse(TokenGenerator.get_token())


@csrf_exempt
def registration_submission(request):

        token = request.META.get('HTTP_X_MOUNTAINHACKS')
        if not token:
            print "no token"
            raise PermissionDenied({"message":"You don't have permission to access"})
        try:
            tokobj = SessionToken.objects.get(val=token)
            tokobj.delete()
        except SessionToken.DoesNotExist:
            print "token does not exist"
            raise PermissionDenied({"message":"You don't have permission to access"})

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

        if out_of_state == "Yes":
            out_of_state = True
        else:
            out_of_state = False

        if first == "Yes":
            first = True
        else:
            first = False

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
