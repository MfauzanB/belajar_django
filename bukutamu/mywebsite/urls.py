from django.contrib import admin
from django.urls.conf import path, include

urlpatterns = [
	path('blog/', include('blog.urls',namespace = 'blog')),
    path('admin/', admin.site.urls),
]
