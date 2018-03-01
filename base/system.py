from django.contrib.auth import authenticate
from django.contrib.auth.mixins import UserPassesTestMixin

class AdminUserMixin(UserPassesTestMixin):
    def auth(self):
        if  self.request.user.is_authenticated:
            return True
        elif self.request.user.is_superuser:
            return True
        else:
            return False