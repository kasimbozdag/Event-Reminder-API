from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    category = models.ForeignKey(Category, related_name='events', on_delete=models.CASCADE)
    reminder_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
