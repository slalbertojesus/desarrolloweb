from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class CustomPasswordValidator():

    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char.isdigit() for char in password):
            raise ValidationError(_('La contraseña debe contener al menos %(min_length)d digito.') % {'min_length': self.min_length})
        if not any(char.isalpha() for char in password):
            raise ValidationError(_('La contraseña debe contener al menos %(min_length)d letra.') % {'min_length': self.min_length})
        if not any(char in special_characters for char in password):
            raise ValidationError(_('La contraseña debe contener al menos %(min_length)d caracteres especiales.') % {'min_length': self.min_length})

    def get_help_text(self):
        return ""

        