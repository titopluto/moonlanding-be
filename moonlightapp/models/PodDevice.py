from django.db import models
from moonlightapp.models.Device import Device
from moonlightapp.models.Pod import Pod as PodModel

class PodDevice(models.Model):
    pod = models.ForeignKey(PodModel, related_name="devices", on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    dev_url = models.CharField(max_length=500)

    def __str__(self):
        return self.dev_url