from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class blogModel(models.Model):
    name=models.CharField(max_length=250)
    text=models.TextField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    time=datetime.now()
    
    def get_absolute_url(self):
        return reverse("details",kwargs={"pk":self.pk})
    
    def __str__(self):
        return self.name