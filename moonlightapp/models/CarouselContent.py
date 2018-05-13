from django.db import models
from moonlightapp.models.Course import Course

def user_file_path(instance, filename):
    return filename

class CarouselContent(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    active = models.BooleanField()
    img = models.FileField(upload_to=user_file_path)
    priority = models.IntegerField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ('priority',)