from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from recipes.models import *

from .serializers import *


class OnlyGetViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    pass


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class FavouriteViewSet(viewsets.ModelViewSet):
    seriaizer_class = MakeFavouriteSerializer

    def get_queryset(self):
        recipes = Recipe.objects.filter(is_favourite=True)
        return recipes
