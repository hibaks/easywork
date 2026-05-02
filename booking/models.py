from django.db import models
from worker.models import Worker
from user.models import User
from temp.models import Service
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # user_id = models.IntegerField()

    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=45)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    # service_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'book'

