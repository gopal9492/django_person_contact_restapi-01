from django.db import models


class contacts(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
