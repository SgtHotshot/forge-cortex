from django.conf.urls import patterns, include, url
from django.contrib import admin

import cortex.core.views

urlpatterns = patterns('',
	url(r'^$', cortex.core.views.RootView.as_view(), name = 'root'),

	url(r'^admin/', include(admin.site.urls)),
)

