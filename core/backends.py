from django.contrib.auth.backends import BaseBackend
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        # Check if the username exists
        # Check if the password is valid
        # If is valid, return user
        # if invalid return None
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            pwd_valid = check_password(password, user.password)
            if user is not  None and pwd_valid == True:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None