from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from moonlightapp.views.Pod import PodList, PodDetail, AllPodDetail
from moonlightapp.views.Document import DocumentList
from moonlightapp.views.Course import CourseList, CouseLabList
from moonlightapp.views.CarouselContent import CarouselContentList

urlpatterns = [
    url(r'^carouselcontent$', CarouselContentList.as_view()),
    url(r'^pods$', PodList.as_view()),
    url(r'^pods/detail/$', AllPodDetail.as_view()),
    url(r'^pods/(?P<pk>[0-9]+)/$', PodDetail.as_view()),
    url(r'^documents$', DocumentList.as_view()),
    url(r'^courses$', CourseList.as_view()),
    url(r'^courses/(?P<pk>[0-9]+)/labs$', CouseLabList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)