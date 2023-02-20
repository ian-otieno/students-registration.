from django.db import models

class Stream(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    admission_number = models.CharField(max_length=30)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.stream})'
