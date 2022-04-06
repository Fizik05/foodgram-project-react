from django.urls import include, path
from rest_framework import routers

from .views import *

app_name = 'api'


router = routers.DefaultRouter()

router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)
#router.register(r'recipes/(?P<id>[\d]+)/favourite', FavouriteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
