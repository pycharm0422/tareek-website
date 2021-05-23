from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields import NullBooleanField
from django.contrib.auth.models import User

class PlanType(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self) -> str:
        return (str(self.width) + 'X' + str(self.height))

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    plantype = models.ForeignKey(PlanType, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/', default='default.jpg')
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title + str(self.id)

class CanAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    pdf = models.TextField(null=True)

    def __str__(self):
        return self.user.username