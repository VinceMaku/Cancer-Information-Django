from django.conf.urls import url
from django.contrib import admin

from .views import (
    comment_thread,
    comment_delete,
    Usercomment_thread,
    Usercomment_delete
    )

urlpatterns = [
    url(r'^(?P<id>\d+)/$', comment_thread, name='thread'),
    url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
    url(r'^(?P<id>\d+)/$', Usercomment_thread, name='Userthread'),
    url(r'^(?P<id>\d+)/delete/$', Usercomment_delete, name='Userdelete'),
]
