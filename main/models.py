
from django.db import models
from django.contrib.auth.models import User





# Create your models here.
class Book(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    files = models.FileField(upload_to='books/pdfs/')
    profile = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.username

    def delete(self, *args, **kwargs):
        self.files.delete()
        self.profile.delete()
        super().delete(*args, **kwargs)
    def edit(self, *args, **kwargs):
        self.files.edit()
        self.profile.edit()
        super().update(*args, **kwargs)
