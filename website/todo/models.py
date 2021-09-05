from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.TextField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
