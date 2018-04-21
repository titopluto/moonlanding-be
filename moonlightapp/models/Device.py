from django.db import models

DEVICES = [
    ('ROUTER', 'Router'), ('SWITCH', 'Switch'), ('ACCESS_POINT', 'Access Point'), ('TS', 'Terminal Server')
]

class Device(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=10, choices=DEVICES)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
