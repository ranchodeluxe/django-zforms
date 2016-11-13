#
#  django imports
from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#
#  system imports
#

#
#  app imports
#
from views import zFormView

urlpatterns = [
    url( r'^$', zFormView.as_view(), None, 'forms-view' ),
]

