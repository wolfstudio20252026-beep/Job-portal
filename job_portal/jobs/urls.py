from django.urls import path
from .views import delete_article, edit_article, jooble_jobs
from .views import (
    home,
    vacancies,
    vacancy_detail,
    articles,
    article_detail,
    add_article,
    about
)

urlpatterns = [
        path(
        "article/<int:id>/edit/",
        edit_article,
        name="edit_article"
    ),

    path(
        "article/<int:id>/delete/",
        delete_article,
        name="delete_article"
    ),
    path(
        "search/",
        jooble_jobs,
        name="jooble_jobs"
    ),
    path(
        "",
        home,
        name="home"
    ),

    path(
        "vacancies/",
        vacancies,
        name="vacancies"
    ),

    path(
        "vacancy/<int:id>/",
        vacancy_detail,
        name="vacancy_detail"
    ),

    path(
        "articles/",
        articles,
        name="articles"
    ),

    path(
        "articles/<int:id>/",
        article_detail,
        name="article_detail"
    ),

    path(
        "add-article/",
        add_article,
        name="add_article"
    ),

    path(
        "about/",
        about,
        name="about"
    ),
]