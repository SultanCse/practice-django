from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

# Create your models here.
class UserProfile(models.Model):
    user_id=models.OneToOneField(User)
    description=models.CharField(max_length=200,default='')
    city=models.CharField(max_length=50,default='')
    age = models.DateField(("Date"), default=datetime.date.today)
    website=models.URLField(default='')
    phone=models.IntegerField(default=0)
    def __str__(self):
        return str(self.user_id) + ' ' + self.city

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.obsects.create(user_id=kwargs['instance'])
post_save.connect(create_profile, sender=User)
