from django.db import models
import uuid


class TypeChoices(models.TextChoices):
    ENTRY = "entry"
    OUTPUT = "output"


class Finance(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    description = models.CharField(max_length=127)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(
        max_length=12, choices=TypeChoices.choices, default=TypeChoices.ENTRY
    )

    list = models.ForeignKey("lists.List", models.CASCADE, "finances")

    category = models.ForeignKey(
        "categories.Category", models.SET_NULL, "finances", null=True
    )
