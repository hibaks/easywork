from django.db import models

# Create your models here.

class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=45)
    reply = models.CharField(max_length=45)
    user_id = models.IntegerField()
    worker_id = models.IntegerField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'complaint'
