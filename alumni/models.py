from django.db import models


class Alumni(models.Model):
    name = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
    phone_number = models.CharField(max_length=11)
    student_class = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.name
