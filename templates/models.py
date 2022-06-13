from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import uuid

UserModel = get_user_model()


class Domain(models.Model):
    _id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    host_name = models.CharField(max_length=1000)
    domain = models.CharField(max_length=1000, blank=True, null=True)
    cname = models.CharField(max_length=1000)
    site = models.ForeignKey(
        'Template', on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Csv(models.Model):
    _id = models.AutoField(primary_key=True)
    csvName = models.CharField(max_length=1000)
    givenUrl = models.CharField(max_length=1000, default="#")
    csvUrl = models.CharField(max_length=1000)
    csvRows = models.IntegerField(default=0)
    csvData = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Images(models.Model):
    _id = models.AutoField(primary_key=True)
    folder = models.CharField(max_length=1000)
    Url = models.CharField(max_length=1000)
    imgLinks = models.TextField()   # its a array of images in str form
    numImg = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Template(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    _id = models.AutoField(primary_key=True)
    publicID = models.CharField(
        max_length=100, blank=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=1000)
    # many to many relation with Folder
    folder = models.ForeignKey(Images, on_delete=models.CASCADE)
    file = models.ForeignKey(Csv, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return '%s %s' % (self.name, self.user.username)


class configTemplate(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    bName = models.CharField(max_length=1024, blank=True)
    bLogo = models.TextField(blank=True)
    bHead = models.CharField(max_length=1024, blank=True)
    bDesc = models.TextField(blank=True)
    bLocation = models.TextField(blank=True)
    bSite = models.TextField(blank=True)
    bCTA = models.CharField(max_length=1024, blank=True)
    bMail = models.CharField(max_length=1024, blank=True)
    bPhone = models.CharField(max_length=16, blank=True)
    rawjson = models.JSONField(blank=True, null=True)
    renderedjson = models.JSONField(blank=True, null=True)
