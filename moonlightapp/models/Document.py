from django.db import models

def user_file_path(instance, filename):
    return instance.name

class Document(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to= user_file_path)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)