from django.db import models


# Create your models here.
class EventOrder(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    sales = models.CharField(max_length=100)
    attendance = models.PositiveIntegerField()
    linen = models.TextField()
    stage = models.TextField()
    notes = models.TextField()
    alcohol = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
