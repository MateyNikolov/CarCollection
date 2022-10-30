from django.core.exceptions import ValidationError


def min_user_age(value):
    if value < 18:
        raise ValidationError('Your age cannot be bellow 18.')


def valid_car_year(value):
    if value < 1980 or value > 2049:
        raise ValidationError('Year must be between 1980 and 2049')
