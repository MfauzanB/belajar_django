from articles.viewsets import ArticlesViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles',ArticlesViewset)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive