from django.db import models

# Create your models here.
class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    skill = models.CharField(max_length=300)
    specialization = models.CharField(max_length=500)
    contact = models.CharField(max_length=15)
    availability = models.CharField(max_length=45)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'worker'

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    bio = models.CharField(max_length=205, blank=True, null=True)
    profile_pic = models.CharField(max_length=405, blank=True, null=True)
    user = models.OneToOneField('Worker', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profile'
