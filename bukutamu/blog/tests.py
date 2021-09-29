from django.http import response
from django.test import TestCase, Client

# Create your tests here.
class Testing123(TestCase):
    def test_url_blog(self):
        response = Client().get('/blog/')
        self.assertEquals(response.status_code, 200)

    def test_templates_blog_index(self):
        response = Client().get('/blog/')
        self.assertTemplateUsed(response, 'blog/index.html')
    
    def test_templates_blog_create(self):
        response = Client().get('/blog/')
        self.assertTemplateUsed(response, 'blog/create.html')

    