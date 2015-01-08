import django.views.generic

# pylint: disable=too-few-public-methods

class RootView(django.views.generic.TemplateView):
	template_name = 'root.html'

