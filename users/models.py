from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=27)
    last_name = None
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False, editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
