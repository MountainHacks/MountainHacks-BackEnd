__author__ = 'Derek Argueta'
__email__  = 'derek@mountainhacks.com'

from random import choice, randrange
from string import letters, digits, punctuation
from api.models import SessionToken, Student

class TokenGenerator():

    @staticmethod
    def generate_string():
        num = randrange(1, 99, 1)
        valid_chars = str(letters) + str(digits) + str(punctuation)
        val = "".join(choice(valid_chars.replace('\'', '').replace('\"', '').replace(';', '').replace('+', '')) for i in range(0, num))
        return val

    @staticmethod
    def generate_url_safe_string():
        num = randrange(1, 99, 1)
        valid_chars = str(letters) + str(digits)
        val = "".join(choice(valid_chars) for i in range(0, num))
        return val

    @staticmethod
    def get_token():
        while True:
            val = TokenGenerator.generate_string()
            try:
                existing_session = SessionToken.objects.get(val=val)
            except SessionToken.DoesNotExist:
                token = SessionToken(val=val)
                token.save()
                return val

    @staticmethod
    def get_confirmation_code():
        while True:
            val = TokenGenerator.generate_url_safe_string()
            try:
                existing_code = Student.objects.get(confirmation_code=val)
            except Student.DoesNotExist:
                return val
