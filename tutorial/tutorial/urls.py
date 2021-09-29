from coba import views
from django.contrib import admin
from django.urls.conf import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bukutamu/', include('coba.urls') ),
]
