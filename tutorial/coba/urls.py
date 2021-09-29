from coba.forms import BuatPesan
from django.urls.conf import path, include
from . import views
urlpatterns = [
    path('pesan/', views.BuatPesan, name='BuatPesan'),
    path('list-pesan/', views.ListPesan, name='ListPesan'),
]
