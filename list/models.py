from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    optional_dead_date = models.DateTimeField(null=True, blank=True)
    boolean_field = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.content
