from json.encoder import py_encode_basestring
from django.conf.urls import url
from django.db.models.aggregates import Count
from django.http import response
from django.shortcuts import get_object_or_404, render
from django.test import TestCase, Client, client
from django.urls import reverse, resolve

from blog.models import PostModel
from blog.views import index, create

from blog.forms import PostForm
import datetime

# Create your tests here.
class Testing123(TestCase):
    def test_url_blog(self):
        response = Client().get('/blog/')
        self.assertEquals(response.status_code, 200)
        
    # def test_url_create(self):
    #     url = reverse('create')
    #     # print(resolve(url))
    #     self.assertEquals(resolve(url).func, create)
    def test_templates_blog_create(self):
        client = Client()
        response = client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/index.html')
        
class TestingModels(TestCase):
    
    def test_kirim_data_models(self):
        #self.kirimdata = PostModel.objects.create(nama="fauzan", pesan="happy")
        PostModel1 = PostModel.objects.create(
            nama="Fatinah", 
            pesan="Happy"
            )
        PostModel2 = PostModel.objects.create(
            nama="fauzan", 
            pesan="good boy"
            )
        GetAllData = PostModel.objects.all()
        hitung_berapa_bukunya = GetAllData.count()
        self.assertEquals(hitung_berapa_bukunya, 2)
        print (hitung_berapa_bukunya)

        print (PostModel1, PostModel2)

    def test_send_data(self):
        nama = PostModel.objects.create(nama = "eza")
        self.assertEqual(str(nama),"1. eza")

    # def test_hitung_jumlah_komentar(self):
    #     self.postingan = self.kirimdata
    #     print (self.postingan)
    # def test_hitung(self):
    #     self.assertEquals(self.kirimdata.slug)

class AuthorListViewTest(TestCase):
    def setUpTestData(cls):
        jumlah_pesan = 2

        for id_pesan in range(jumlah_pesan):
            PostModel.objects.create(
                nama =f'fauzan {id_pesan}',
                pesan =f'happy {id_pesan}',
            )

    def test_view_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_view_name(self):
        response = self.client.get(reverse('blog:create'))
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get(reverse('blog:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/create.html')

# class test_form(TestCase):

#     def test_date(self):
#         date = datetime.date.today()
#         form = PostForm(data={'renewal_date': date})
#         self.assertTrue(form.is_valid())