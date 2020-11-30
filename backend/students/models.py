from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    rating = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"Student: {self.name}"
