from rest_framework import serializers

from recipes.models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'color', 'slug')
        model = Tag


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'measurement_unit',)
        model = Ingredient


class MakeFavouriteSerializer(serializers.ModelSerializer):
 #   class Meta:
    pass
