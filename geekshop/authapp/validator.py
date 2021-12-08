from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_size(value):
    if value.size > 1048576:
        raise ValidationError(_(f'Слишком большой файл! Выберите файл не больше 1 МБ'), params={'value': value},)

