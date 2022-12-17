# django 
from django.db import models

# directories
from design.models import Design_Model
# from user.models import User

class Comment(models.Model):
    design = models.ForeignKey(Design_Model, on_delete = models.CASCADE)
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    verified = models.BooleanField(default = True)
    reported = models.IntegerField(default = 0)

