import django.shortcuts
import django.conf
import django.contrib.auth
import django.contrib.auth.forms
import django.core.urlresolvers
import django.views.generic

# pylint: disable=too-few-public-methods, too-many-ancestors, unused-argument

class RootView(django.views.generic.TemplateView):
	template_name = 'root.html'
	
class DashboardView(django.views.generic.TemplateView):
	template_name = 'dashboard.html'
	
class ModDashboardView(django.views.generic.TemplateView):
	template_name = 'modDashboard.html'
	
class ModAddEditView(django.views.generic.TemplateView):
	template_name = 'modAddEdit.html'
	
class ModVersionAddEditView(django.views.generic.TemplateView):
	template_name = 'modVersionAddEdit.html'

class LoginView(django.views.generic.FormView):
	form_class    = django.contrib.auth.forms.AuthenticationForm
	redirect_arg  = 'next'
	template_name = 'login.html'

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated():
			return django.shortcuts.redirect(self.get_success_url())

		return super(LoginView, self).get(*args, **kwargs)

	def get_success_url(self):
		request_params = getattr(self.request, self.request.method)

		if self.redirect_arg in request_params:
			return request_params[self.redirect_arg]
		elif self.redirect_arg in self.kwargs:
			return self.kwargs[self.redirect_arg]
		else:
			return django.conf.settings.LOGIN_REDIRECT_URL

	def form_valid(self, form):
		django.contrib.auth.login(self.request, form.get_user())

		return super(LoginView, self).form_valid(form)

class LogoutView(django.views.generic.View):
	redirect_url = django.core.urlresolvers.reverse_lazy('root')

	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)

	def post(self, *args, **kwargs):
		django.contrib.auth.logout(self.request)

		return django.shortcuts.redirect(self.redirect_url)

