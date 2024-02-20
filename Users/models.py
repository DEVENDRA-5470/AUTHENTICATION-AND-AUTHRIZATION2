from django.db import models

class Course(models.Model):
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    duration_in_weeks = models.IntegerField()
    start_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
