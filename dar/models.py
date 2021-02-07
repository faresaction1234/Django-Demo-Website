from django.db import models

# Create your models here.
class work(models.Model):
    work_type = models.CharField(max_length=250)
    hours = models.IntegerField(default=0)
    def __str__(self):
        return self.work_type+'('+str(self.hours)+')'


