from django.db.models.aggregates import Count
from django.http import response
from django.test import TestCase, Client

from blog.models import PostModel

# Create your tests here.
# class Testing123(TestCase):
#     def test_url_blog(self):
#         response = Client().get('/blog/')
#         self.assertEquals(response.status_code, 200)
    
#     def test_templates_blog_create(self):
#         response = Client().get('/blog/')
#         self.assertTemplateUsed(response, 'blog/create.html')
        
class TestingModels(TestCase):
    
    def test_kirim_data_models(self):
        #self.kirimdata = PostModel.objects.create(nama="fauzan", pesan="happy")
        PostModel.objects.create(
            nama="INI NAMA", 
            pesan="INI PESAN"
            )
        hitung_berapa_bukunya = PostModel.objects.all().count()
        self.assertEquals(hitung_berapa_bukunya, 1)
        print (hitung_berapa_bukunya)

    # def test_hitung_jumlah_komentar(self):
    #     self.postingan = self.kirimdata
    #     print (self.postingan)
    # def test_hitung(self):
    #     self.assertEquals(self.kirimdata.slug)
