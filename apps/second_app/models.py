from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
import re 
import bcrypt


class Friend(models.Model):
    user_friend = models.ForeignKey(User, related_name='first')
    second_friend = models.ForeignKey(User, related_name='second')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



