from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control r-input col-12"
        self.fields["username"].widget.attrs["placeholder"] = "Enter username"
        self.fields["password"].widget.attrs["class"] = "r-pass col-11"
        self.fields["password"].widget.attrs["placeholder"] = "Enter password"

    # def clean_username(self):
    #     data = self.cleaned_data["username"]
    #     return data.lower()
