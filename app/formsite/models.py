from django.db import models

PETS = [
    ('cat','Cats'),
    ('dog','Dogs')
]

class UserData(models.Model):
    Name  = models.CharField(max_length=100, unique=True, verbose_name="User Name")
    Color = models.CharField(max_length=20,verbose_name="Eye Color")
    Pet   = models.CharField(max_length=10,choices=PETS,default='cat',verbose_name="Pet Preference")
    users = models.Manager()