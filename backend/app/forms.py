from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django import forms
from django.utils.translation import gettext_lazy as _


class AuthAdminForm(AuthenticationForm):
    password = None

    error_messages = {
        "invalid_login": _(
            "Please enter a correct admin Token."
        ),
        "inactive": _("This account is inactive."),
    }

    def clean(self):
        username = self.cleaned_data.get("username")

        if username is not None:
            self.user_cache = authenticate(
                self.request, username=username
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data