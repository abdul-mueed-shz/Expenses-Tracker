from django.contrib.auth.models import User
from django.db import models

from apps.common.models import BaseModel


# Create your models here.
class Expense(BaseModel):
    amount = models.IntegerField(max_length=255)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
