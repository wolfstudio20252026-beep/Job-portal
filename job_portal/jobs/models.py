from django.db import models


class Vacancy(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Назва вакансії"
    )

    company = models.CharField(
        max_length=200,
        verbose_name="Компанія"
    )

    location = models.CharField(
        max_length=200,
        verbose_name="Місто"
    )
    views = models.PositiveIntegerField(
    default=0,
    verbose_name="Просмотры"
    )

    experience = models.CharField(
        max_length=100,
        verbose_name="Досвід"
    )

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Зарплата"
    )

    description = models.TextField(
        verbose_name="Опис"
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
    )

    short_description = models.TextField(
        verbose_name="Короткий опис"
    )

    content = models.TextField(
        verbose_name="Текст статті"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title