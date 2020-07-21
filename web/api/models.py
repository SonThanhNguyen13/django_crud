from django.db import models

# Create your models here.


class DataTable(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.CharField(max_length=5000)
    status = models.IntegerField(choices=((1,1,), (2,2,)), default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

