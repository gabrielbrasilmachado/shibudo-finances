from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


# Create your models here.
class MonthChoices(models.TextChoices):
    JANUARY = "january"
    FEBRUARY = "february"
    MARCH = "march"
    APRIL = "april"
    MAY = "may"
    JUNE = "june"
    JULY = "july"
    AUGUST = "august"
    SEPTEMBER = "september"
    OCTOBER = "october"
    NOVEMBER = "november"
    DECEMBER = "december"


class List(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    month = models.CharField(max_length=20, choices=MonthChoices.choices)
    year = models.PositiveIntegerField(
        validators=[MaxValueValidator(2200), MinValueValidator(1900)]
    )

    user = models.ForeignKey("users.User", models.CASCADE, "lists")
