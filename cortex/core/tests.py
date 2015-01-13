from django.test import TestCase, TransactionTestCase

# pylint: disable=too-few-public-methods

class RootViewTestCase(TestCase):
	def test_guest_accessible(self):
		response = self.client.get('/')
		self.assertEquals(
			response.status_code,
			200,
		)

		self.assertTemplateUsed(
			response      = response,
			template_name = 'root.html',
		)

class LoginViewTestCase(TransactionTestCase):
	fixtures = ['test_user.json']

	def test_guest_accessible(self):
		response = self.client.get('/login')
		self.assertEquals(
			response.status_code,
			200,
		)

		self.assertTemplateUsed(
			response      = response,
			template_name = 'login.html',
		)

	def test_login_success(self):
		response = self.client.post(
			'/login',
			{
				'username': 'test_user',
				'password': 'test',
			},
		)

		self.assertRedirects(
			response,
			'/',
		)

		self.client.logout()

	# TODO: we need another page to test redirects...
	#def test_login_redirect(self):
		#response = self.client.post('/login', {'username': 'test_user', 'password': 'test', 'next': ''})

		#self.assertRedirects(
			#response,
			#'',
		#)

		#self.client.logout()

	def test_login_error(self):
		response = self.client.post(
			'/login',
			{
				'username': 'test_user',
				'password': 'bad_password',
			},
		)

		self.assertFormError(
			response,
			'form',
			None,
			[
				'Please enter a correct username and password. Note that both fields may be case-sensitive.',
			],
		)

	def test_login_skip(self):
		self.client.login(username = 'test_user', password = 'test')

		response = self.client.get('/login')

		self.assertRedirects(
			response,
			'/',
		)

