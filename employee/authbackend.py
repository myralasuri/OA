from django.contrib.auth.backends import ModelBackend
from employee.models import Employe

class AuthBackend(ModelBackend):
    def authenticate(self=None, request=None, username=None, password=None):
        emp = Employe.objects.get(email = username,pin = password)
        print("at authenticvate backend", emp)
        if emp is not None:
            return emp
        return LookupError('user name / password is incorrect')
