from django.db import models

class Workout(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration_min = models.IntegerField(default=30)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
