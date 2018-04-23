from django.db import models
from moonlightapp.models.Device import Device

class Pod(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    devices = models.ManyToManyField(Device, through='PodDevices')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class PodDevices(models.Model):
    pod = models.ForeignKey(Pod, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    dev_url = models.CharField(max_length=500)