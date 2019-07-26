from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField('NAME', max_length=5, blank=True)
    todo = models.CharField('TODO', max_length=20)

    def __str__(self):
        return self.todo

    def save(self, force_insert=False, force_update=False, using=None, update_field=None):

        if not self.name:
            self.name = "KB관리자"
        super().save()
        

