from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User

class Box(models.Model):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    last_modified_by=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE,related_name='last_modified_by')
    id=models.AutoField(primary_key=True)
    length=models.IntegerField(default=0,blank=True,null=True)
    width=models.IntegerField(default=0,blank=True,null=True)
    height=models.IntegerField(default=0,blank=True,null=True)
    created_on = models.DateField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified_on = models.DateField(auto_now=True, editable=False, null=False, blank=False)
    volume=models.IntegerField(default=0)
    area=models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id)
 
    
    

