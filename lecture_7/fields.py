from django.db import models



class BooleanChoiceField(models.BooleanField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] =(
            (True, 'Available'),
            (False, 'Not Available')
        )

        kwargs['default'] = True
        super().__init__(*args, **kwargs)