# Generated by Django 3.2.12 on 2022-04-10 18:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("recipes", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор рецепта",
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(
                related_name="recipes",
                through="recipes.IngredientAmount",
                to="recipes.Ingredient",
                verbose_name="Ингридиенты",
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="tags",
            field=models.ManyToManyField(
                to="recipes.Tag", verbose_name="Теги"
            ),
        ),
        migrations.AddField(
            model_name="ingredientamount",
            name="ingredient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.ingredient",
                verbose_name="Ингридиент",
            ),
        ),
        migrations.AddField(
            model_name="ingredientamount",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.recipe",
                verbose_name="Рецепт",
            ),
        ),
        migrations.AddConstraint(
            model_name="ingredient",
            constraint=models.UniqueConstraint(
                fields=("name", "measurement_unit"), name="unique_ingredient"
            ),
        ),
        migrations.AddField(
            model_name="favorite",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorites",
                to="recipes.recipe",
                verbose_name="Рецепт",
            ),
        ),
        migrations.AddField(
            model_name="favorite",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart",
                to="recipes.recipe",
                verbose_name="Рецепт",
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddConstraint(
            model_name="ingredientamount",
            constraint=models.UniqueConstraint(
                fields=("ingredient", "recipe"),
                name="unique ingredients recipe",
            ),
        ),
        migrations.AddConstraint(
            model_name="favorite",
            constraint=models.UniqueConstraint(
                fields=("user", "recipe"),
                name="unique favorite recipe for user",
            ),
        ),
        migrations.AddConstraint(
            model_name="cart",
            constraint=models.UniqueConstraint(
                fields=("user", "recipe"), name="unique cart user"
            ),
        ),
    ]
