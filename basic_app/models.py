from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from phone_field import PhoneField



# Create your models here.

class ShopKeeperRegistration(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #Additional Fields
    phone_number = PhoneField(blank=True,help_text='Contact phone number with country code')
    #number = models.IntegerField()
    

    def __str__(self):
        return self.user.username


class UserFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    Feedback = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

