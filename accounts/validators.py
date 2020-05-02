from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _, ngettext
from django.utils.translation import ugettext as _

class MinimumLengthValidator:

    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "La contraseña es muy corta. Debe contener al menos %(min_length)d caracter.",
                    "La contraseña es muy corta. Debe contener al menos %(min_length)d caractéres.",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return ngettext(
            "Tu contraseña debe contener al menos %(min_length)d caracter.",
            "Tu contraseña debe contener al menos %(min_length)d caracteres.",
            self.min_length
        ) % {'min_length': self.min_length}

class NumericPasswordValidator:

    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _("La contraseña solo tiene números."),
                code='password_entirely_numeric',
            )

    def get_help_text(self):
        return _('La contraseña no puede contener solo números.')
