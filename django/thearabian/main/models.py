from django.db import models


class country(models.Model):
    name = models.CharField(max_length=64, default="Soon")
    title = models.CharField(max_length=64, default="Soon")

    def __str__(self):
        return f"{self.id}. {self.name}"
