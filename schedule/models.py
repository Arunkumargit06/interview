from django.db import models
from django.contrib.auth.models import User,Group,Permission

# Create your models here.
class UserDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    mobile = models.CharField(max_length=30)

    class Meta:
        db_table = "cand_detail"

class UserSchdulemaaping(models.Model):
    user_detail = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    time_start= models.DateTimeField()
    time_end= models.DateTimeField() 

    class Meta:
        db_table = "schedulemapping"

