from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.



class PhoneModel(models.Model):
    name = models.CharField(max_length=100,default='')
    power = models.CharField(max_length=200,default='')
    creator_name = models.CharField(max_length=200,default='')
    created_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    class Meta:
        db_table = "PhoneModel"
    def __str__(self) -> str:
        return self.name