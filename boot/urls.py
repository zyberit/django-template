"""boot URL Configuration
"""

from django.conf.urls import url
from .views import bootstrap, ping

urlpatterns = [
    url(r'^bootstrap', bootstrap, name="bootstrap"),
    url(r'^ping', ping, name="ping"),
]
