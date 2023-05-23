from django.db import models


# Create your models here.
class BaseModel(models.Model):
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
