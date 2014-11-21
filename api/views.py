__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

from api.models import Student, Company, SessionToken
from api.serializers import StudentSerializer, CompanySerializer

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from api.tokens import TokenGenerator
from rest_framework.exceptions import PermissionDenied
from django.core.mail import send_mass_mail

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

def confirmAttendee(request):
    """ Accepts a parameter called 'code', representing a unique confirmation code. It is used to look up a student. If
        we get a student back, then it is a good confirmation code. We then set the student's is_confirmed bit to true
    """

    confirmation_code = request.GET.get("code")
    if not confirmation_code:
        return HttpResponse(status=404)

    print confirmation_code
    try:
        student = Student.objects.get(confirmation_code=confirmation_code)
        student.is_confirmed = True
        student.save()
        return redirect("http://www.mountainhacks.com/thanks.html")
    except Student.DoesNotExist:
        return HttpResponse(status=403)

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
        resume = request.FILES.get('resume')

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
                          first_hackathon=first,
                          resume=resume,
                          confirmation_code=TokenGenerator.get_confirmation_code())
        student.save()

        message = "%s %s has registered for MountainHacks 2015!" % (first_name, last_name)
        subject = "New Registrant!"
        message1 = (subject, message, "mountainhacks@gmail.com", ["mountainhacks@gmail.com",])
        message2 = ("MountainHacks 2015 Confirmation", "Thanks for registering! Please confirm this email by clicking on the following link: http://www.mountainhacks.com/api/confirm?code="+student.confirmation_code, "mountainhacks@gmail.com", [email,])
        send_mass_mail((message1, message2), fail_silently=False)

        return HttpResponse(status=201)
