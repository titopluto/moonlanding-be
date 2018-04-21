from django.urls import path
from moonlightapp.views.userview import UserListCreateAPIView
from moonlightapp.views.Pod import PodList

urlpatterns = [
    path(r'user', UserListCreateAPIView.as_view()), #the path for our index view
    path(r'pod', PodList.as_view())
]