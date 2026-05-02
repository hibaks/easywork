from django.db import models
from user.models import User
# Create your models here.

from worker.models import Worker
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    rating = models.CharField(max_length=45)
    comment = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    # user_id = models.IntegerField(blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'feedback'

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.CharField(max_length=75)
    date = models.DateField()
    # worker_id = models.IntegerField(blank=True, null=True)
    worker=models.ForeignKey(Worker,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'review'

