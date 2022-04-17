from django.core import validators
from django.db import models
from users.models import User


class Tag(models.Model):
    BLUE = "#0000FF"
    ORANGE = "#FFA500"
    GREEN = "#008000"
    PURPLE = "#800080"
    YELLOW = "#FFFF00"

    COLOR_CHOICES = [
        (BLUE, "Синий"),
        (ORANGE, "Оранжевый"),
        (GREEN, "Зеленый"),
        (PURPLE, "Фиолетовый"),
        (YELLOW, "Желтый"),
    ]
    name = models.CharField(
        max_length=200, unique=True, verbose_name="Название тега"
    )
    color = models.CharField(
        max_length=7,
        unique=True,
        choices=COLOR_CHOICES,
        verbose_name="Цвет в HEX",
    )
    slug = models.SlugField(
        max_length=200, unique=True, verbose_name="Уникальный слаг"
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Тег"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField("Название ингредиента", max_length=150)
    measurement_unit = models.CharField(max_length=25)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Ингредиент"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "measurement_unit"], name="unique_ingredient"
            )
        ]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipes",
        verbose_name="Автор рецепта",
    )
    name = models.CharField(max_length=200, verbose_name="Название рецепта")
    image = models.ImageField(
        upload_to="recipes/", verbose_name="Картинка рецепта"
    )
    text = models.TextField(verbose_name="Описание рецепта")
    ingredients = models.ManyToManyField(
        Ingredient,
        through="IngredientAmount",
        verbose_name="Ингридиенты",
        related_name="recipes",
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name="Теги",
    )
    cooking_time = models.IntegerField(
        validators=(
            validators.MinValueValidator(
                1, message="Блюдо готовится минимум 1 минуту"
            ),
        ),
        verbose_name="Время приготовления",
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Рецепт"


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name="Ингридиент",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name="Рецепт",
    )
    amount = models.IntegerField(
        validators=(
            validators.MinValueValidator(
                1, message="Минимальное количество ингридиентов 1"
            ),
        ),
        verbose_name="Количество",
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Количество ингридиента"
        constraints = [
            models.UniqueConstraint(
                fields=["ingredient", "recipe"],
                name="unique ingredients recipe",
            )
        ]


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name="Рецепт",
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Избранное"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "recipe"],
                name="unique favorite recipe for user",
            )
        ]


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name="Пользователь",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name="Рецепт",
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Корзина"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "recipe"], name="unique cart user"
            )
        ]
