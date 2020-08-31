from django.db import models


class djangoClasses(models.Model):
    Title = models.CharField(max_length=100)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=50)
    Duration = models.FloatField()

    object = models.Manager()

    def __str__(self):
        return self.Title
