from django.db import models

# Create your models here.


class Developer(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='games')

    def __str__(self):
        return self.title

