from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    disease = models.CharField(max_length=255)

    def __str__(self):
        return self.name
