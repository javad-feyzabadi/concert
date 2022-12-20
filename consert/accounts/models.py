from django.db import models
from django.contrib.auth.models import User 

class ProfileModel(models.Model):
    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل'
    user = models.OneToOneField(User , on_delete =models.CASCADE,verbose_name = 'کاربری',related_name = 'profile')
    
    man = 1
    woman = 2
    status_choices = (
        (man,'مرد'),
        (woman,'زن')
    )
    gender =models.IntegerField(choices = status_choices,verbose_name='جنسیت')
    profileimage = models.ImageField(upload_to = 'profileimage/',verbose_name='عکس پروفایل')
    credit = models.IntegerField(default=0 , verbose_name ='اعتبار')
    