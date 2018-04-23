from django.contrib import admin
from moonlightapp.models.usermodel import User
from moonlightapp.models.Pod import Pod, PodDevices
from moonlightapp.models.Device import Device

admin.site.register(User)
admin.site.register(Pod)
admin.site.register(Device)
admin.site.register(PodDevices)