from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from CarCollection.car_app.validators import min_user_age, valid_car_year


class Profile(models.Model):

    MIN_USERNAME_LENGTH = 2
    MIN_USERNAME_LENGTH_VALIDATOR = MinLengthValidator(MIN_USERNAME_LENGTH)
    MIN_USERNAME_LENGTH_VALIDATOR.message = 'The username must be a minimum of 2 chars'
    MAX_USERNAME_LENGTH = 10
    MAX_PASSWORD_FIRST_AND_LAST_NAME_LENGTH = 30

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MIN_USERNAME_LENGTH_VALIDATOR,
        ),
        null=False,
        blank=False,

    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        validators=(
            min_user_age,
        ),
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=MAX_PASSWORD_FIRST_AND_LAST_NAME_LENGTH,
    )
    first_name = models.CharField(
        max_length=MAX_PASSWORD_FIRST_AND_LAST_NAME_LENGTH,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length= MAX_PASSWORD_FIRST_AND_LAST_NAME_LENGTH,
        blank=True,
        null=True,
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Car(models.Model):

    MAX_CAR_TYPE_LENGTH = 10
    MAX_CAR_MODEL_LENGTH = 20

    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER_CAR_TYPE = 'Other'

    CAR_TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER_CAR_TYPE, OTHER_CAR_TYPE),
    )

    type = models.CharField(
        max_length=MAX_CAR_TYPE_LENGTH,
        choices=CAR_TYPES,
        blank=False,
        null=False,
    )
    model = models.CharField(
        max_length=MAX_CAR_MODEL_LENGTH,
        validators=(
            MinLengthValidator(2),
        ),
        blank=False,
        null=False,
    )
    year = models.IntegerField(
        validators=(
            valid_car_year,
        ),
        blank=False,
        null=False,
    )
    image_url = models.URLField(
        blank=False,
        null=False,
    )
    price = models.FloatField(
        validators=(
            MinValueValidator(1.00),
        ),
        blank=False,
        null=False,
    )
