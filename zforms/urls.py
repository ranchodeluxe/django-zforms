#
#  django imports
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.messages import get_messages
from django.shortcuts import render_to_response

#
#  system imports
#
from os import path

#
#  app imports
#
from views import zFormView

urlpatterns = patterns('',
    url( r'^$', zFormView.as_view(), None, 'forms-view' ),
)

