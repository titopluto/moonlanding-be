from django.db import models
from moonlightapp.models.Course import Course

def user_file_path(instance, filename):
    course_id = str(instance.course.id)
    name = instance.name.replace(" ", "_")
    return course_id + "/" + name

class Lab(models.Model):
    course = models.ForeignKey(Course, related_name='lab', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    manual_file = models.FileField(upload_to=user_file_path)

    def __str__(self):
        return str(self.course.id)