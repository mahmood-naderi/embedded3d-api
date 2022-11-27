from django.db import models

class Design_Model(models.Model):
    image = models.ImageField(upload_to = "files/items", null = True)
    content = models.TextField(null = True)
    creator = models.CharField(default = 'Admin', max_length = 20)
    name = models.CharField(null = True, max_length = 25)
    description = models.TextField(null = True)
    date_created = models.DateField(auto_now = True)
    like = models.IntegerField(default = 0)
    dislike = models.IntegerField(default = 0)
    url = models.TextField(null = True)

class Item_Model(models.Model):
    image = models.ImageField(upload_to = "files/items")
    content = models.TextField(null = True)
    description = models.TextField(null = True)
    date_added = models.DateTimeField(auto_now = True)
    name = models.CharField(null = True, max_length = 25)
    company = models.CharField(null = True, max_length = 25)
