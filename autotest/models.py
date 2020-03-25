from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.CharField(max_length=32, unique=True)
    pwd = models.CharField(max_length=32)
    ticket = models.CharField(max_length=32, null=True)


class Confs(models.Model):
    username = models.CharField(max_length=20, unique=True, default='admin')
    rule = models.CharField(max_length=20)
    api_data = models.CharField(max_length=256)
    api_report = models.CharField(max_length=256)
    process_data = models.CharField(max_length=256)
    process_report = models.CharField(max_length=256)
    smtp_host = models.CharField(max_length=50)
    from_addr = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    to_addr = models.CharField(max_length=256)
