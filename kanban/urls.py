from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'^(?P<path>[\w_-]+)$', views.board),
    re_path(r'^(?P<path>[\w_-]+)+/done/$', views.done),
    re_path(r'^(?P<path>[\w_-]+)+/backlog/$', views.backlog),
    re_path(r'^(?P<path>[\w_-]+)+/issue/(?P<issue_id>\d+)$', views.issue_detail),
    re_path(r'^(?P<path>[\w_-]+)+/issue/(?P<issue_id>\d+)$', views.issue_edit),
]