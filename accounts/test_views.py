from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

# Create your tests here.
class TestAccountsViews(TestCase):
    
    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        
    def test_get_register_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
        
    def test_get_profile_page(self):
        test_user = User.objects.create_user(username="test", email="test@example.com", password="Madetotest")
        self.client.login(username='test', password='Madetotest')
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
    
    def test_index_page_load(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_logout(self):
        response = self.client.get("/accounts/logout/")
        self.assertRedirects(response, '/accounts/login/?next=/accounts/logout/', status_code=302, target_status_code=200, fetch_redirect_response=True)
    
    def test_user_can_log_in(self):
        test_user = User.objects.create_user(username="test", email="test@example.com", password="Madetotest")
        response = self.client.post("/accounts/login/", {
            'username': 'test',
            'password': 'Madetotest'
        })
        self.assertRedirects(response, '/accounts/profile/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
        
    def test_user_cant_open_login_if_already_logged_in(self):

        #https://stackoverflow.com/questions/7502116/how-to-use-session-in-testcase-in-django
        test_user =User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        page = self.client.get("/accounts/login/")
        
        self.assertRedirects(page, '/accounts/profile/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)       
    
    def test_user_logout(self):
        #https://stackoverflow.com/questions/7502116/how-to-use-session-in-testcase-in-django
        test_user =User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        page = self.client.get("/accounts/logout/")
        
        self.assertRedirects(page, '/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)  
    
    def test_error_on_login(self):
        response = self.client.post("/accounts/login/", {
            'username': 'test',
            'password': 'Madetotest'
        })
        
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your username or password is incorrect!')
        
    def test_user_can_register(self):
        response = self.client.post("/accounts/register/", {
            'username': 'test',
            'email': 'test@email.com',
            'password1': 'Madetotest',
            'password2': 'Madetotest'
        })
        self.assertRedirects(response, '/accounts/profile/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_error_on_registration(self):
        form_params={
            'username': 'test',
            'email': 'test@email.com',
            'password1': 'Madtotest',
            'password2': 'Madetotest'
        }
        response = self.client.post("/accounts/register", form_params)
        form = UserRegistrationForm(form_params)
        self.assertFalse(form.is_valid())
