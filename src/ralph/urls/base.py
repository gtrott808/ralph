# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import include, url

from ralph.admin import ralph_site as admin

urlpatterns = [
    url(r'^', include(admin.urls)),
    url(r'^api/', include('ralph.dc_view.urls.api')),
    url(r'^api/', include('ralph.data_center.urls.api')),
    url(r'^', include('ralph.dc_view.urls.ui')),
]