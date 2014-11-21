# Must go in the project's root folder

from django.core.mail import send_mass_mail
from django.template.loader import render_to_string
from django.core.mail import get_connection, EmailMultiAlternatives
from api.models import Student
import os

# constants
SUBJECT = "MountainHacks Registration Update and Confirmation"
FROM_EMAIL = "mountainhacks@gmail.com"

# Django settins
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MountainHacks.settings")

registered_students = Student.objects.all()
email_collection = []
for student in registered_students:
	html_content = render_to_string('index.html', {'name': student.first_name})
	text_content = "Hey there %s,\n\nWe recently updated our registration form so that now students can upload their resume with their application. Why would you guys want to do that? Well we're going to supply our sponsoring companies with all the resumes collected, so if you're still looking for an internship or full-time placement, this might be a great way to get an advantage! If you're interested in having your resume included, please respond to this email using the email you used to register (or include the email in the message) and attach your resume so that we can put it in our collection.\n\nEven if you're not interested in submitting your resume, please respond a blank message so that we can confirm this email. (We now have automatic email confirmation for future registrations)\n\nAnd lastly, if you have a Facebook go join the MountainHacks 2015 Attendees group! There, you can chat about different project ideas and find a team for the event.\n\nCan't wait to see you in February!\n\n- The MountainHacks Team" % student.first_name
	msg = EmailMultiAlternatives(SUBJECT, text_content, FROM_EMAIL, [student.email, FROM_EMAIL])
	msg.attach_alternative(html_content, "text/html")

	connection = get_connection()	# Use SMTP server specifiec in settings.py
	connection.open()
	msg.send()
	connection.close()		# Cleanup