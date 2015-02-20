from django.conf.urls import patterns, include, url
from django.contrib import admin

import cortex.core.views

# pylint: disable=invalid-name

urlpatterns = patterns('',
	url(
		r'^$',
		cortex.core.views.RootView.as_view(),
		name = 'root',
	),
	url(
		r'^login$',
		cortex.core.views.LoginView.as_view(),
		name = 'login',
	),
	url(
		r'^logout',
		cortex.core.views.LogoutView.as_view(),
		name = 'logout',
	),
	url(
		r'^admin/',
		include(admin.site.urls),
	),
	url(
		r'^dashboard',
		cortex.core.views.DashboardView.as_view(),
		name = 'dashboard',
	),
	url(
		r'^modDashboard',
		cortex.core.views.ModDashboardView.as_view(),
		name = 'modDashboard',
	),
	url(
		r'^modAddEdit',
		cortex.core.views.ModAddEditView.as_view(),
		name = 'modAddEdit',
	),
	url(
		r'^modVersionAddEdit',
		cortex.core.views.ModVersionAddEditView.as_view(),
		name = 'modVersionAddEdit',
	),
)

