from django.contrib import admin


from moonlightapp.models.Pod import Pod
from moonlightapp.models.PodDevice import PodDevice
from moonlightapp.models.Device import Device

from moonlightapp.models.Document import Document

from moonlightapp.models.Course import Course
from moonlightapp.models.Lab import Lab

from moonlightapp.models.CarouselContent import CarouselContent


admin.site.register(Pod)
admin.site.register(Device)
admin.site.register(PodDevice)

admin.site.register(Document)

admin.site.register(Course)
admin.site.register(Lab)

admin.site.register(CarouselContent)