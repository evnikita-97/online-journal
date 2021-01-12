from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=100, unique=True)
    mail_id=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    
class Journal(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    summary=models.TextField()
    a_date=models.DateTimeField(auto_now_add=True)
    #title=models.TextField(null=True)


