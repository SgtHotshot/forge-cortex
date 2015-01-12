from django.test import TestCase

class RootViewTestCase(TestCase):
	def test_guest_accessible(self):
		self.assertEquals(
			self.client.get('/').status_code,
			200
		)

