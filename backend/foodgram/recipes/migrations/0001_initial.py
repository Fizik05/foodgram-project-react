# Generated by Django 3.2.12 on 2022-04-10 18:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Корзина",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Favorite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Избранное",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=150, verbose_name="Название ингредиента"
                    ),
                ),
                ("measurement_unit", models.CharField(max_length=25)),
            ],
            options={
                "verbose_name": "Ингредиент",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="IngredientAmount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                1,
                                message="Минимальное количество ингридиентов 1",
                            )
                        ],
                        verbose_name="Количество",
                    ),
                ),
            ],
            options={
                "verbose_name": "Количество ингридиента",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=200, verbose_name="Название рецепта"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="recipes/", verbose_name="Картинка рецепта"
                    ),
                ),
                ("text", models.TextField(verbose_name="Описание рецепта")),
                (
                    "cooking_time",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, message="Блюдо готовится минимум 1 минуту"
                            )
                        ],
                        verbose_name="Время приготовления",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рецепт",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=200,
                        unique=True,
                        verbose_name="Название тега",
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("#0000FF", "Синий"),
                            ("#FFA500", "Оранжевый"),
                            ("#008000", "Зеленый"),
                            ("#800080", "Фиолетовый"),
                            ("#FFFF00", "Желтый"),
                        ],
                        max_length=7,
                        unique=True,
                        verbose_name="Цвет в HEX",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=200,
                        unique=True,
                        verbose_name="Уникальный слаг",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тег",
                "ordering": ["-id"],
            },
        ),
    ]
