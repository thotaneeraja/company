from django.db import models
class next(models.Model):
    name=models.CharField(max_length=20)

    age=models.IntegerField(max_length=20)
    email=models.CharField(max_length=20)


    def __str__(self):
        return self.name


# Create your models here.
