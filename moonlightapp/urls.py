from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from moonlightapp.views.userview import UserListCreateAPIView
from moonlightapp.views.Pod import PodList, PodDetail

urlpatterns = [
    url(r'user', UserListCreateAPIView.as_view()), #the path for our index view
    url(r'pod', PodList.as_view()),
    url(r'pods/(?P<pk>[0-9]+)/$', PodDetail.as_view())
]


# urlpatterns = format_suffix_patterns(urlpatterns)