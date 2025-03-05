import json
from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models



class HexField(models.CharField):
    description = 'A hexadecimal field'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 8
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'INTEGER'

    def get_prep_value(self, value):
        if value is None:
            return None
        return int(value, 16)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return format(value, 'x')




class UnixTimestampField(models.DateTimeField):

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return datetime.fromtimestamp(value)

    def to_python(self, value):
        if isinstance(value, datetime):
            return value
        if value is None:
            return None
        return datetime.fromtimestamp(value)

    def get_prep_value(self, value):
        if value is None:
            return None
        return int(value.timestamp())

    def db_type(self, connection):
        return 'INTEGER'



class JSONTextField(models.TextField):

    def to_python(self, value):
        if isinstance(value, dict):
            return value
        if value is None:
            None
        return json.loads(value)


class PisitiveIntegerrFied(models.IntegerField):
    def validate(self, value, model_instance):
        if value < 0:
            raise ValidationError("Value muste be a positive integer")
        super().validate(value, model_instance)


class LowercaseCharField(models.CharField):

    def __init__(self, *args, enforce_lowercase=True, **kwargs):
        self.enforce_lowercase = enforce_lowercase
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['enforce_lowercase'] = self.enforce_lowercase
        return name, path, args, kwargs