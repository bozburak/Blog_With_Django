from django.conf.urls import url
from .views import post_detail

urlpatterns = [
    url(r'^(?P<id>\d+)/$', post_detail),
]