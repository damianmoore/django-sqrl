from django.contrib.auth.models import User
from django.db import models


class SqrlClient(models.Model):
    vuk = models.CharField(max_length=90, unique=True, help_text='Verify Unlock Key')
    user = models.ForeignKey(User)
