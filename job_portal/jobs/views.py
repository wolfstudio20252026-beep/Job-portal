from django.shortcuts import render, get_object_or_404, redirect

from .models import Vacancy, Article
from .forms import ArticleForm
from django.shortcuts import render
from .services import search_jobs
from django.db.models import Q

vacancies_count = Vacancy.objects.count()
articles_count = Article.objects.count()
def jooble_jobs(request):
    keyword = request.GET.get("keyword", "")
    location = request.GET.get("location", "")

    jobs = []

    if keyword or location:
        data = search_jobs(
            keywords=keyword,
            location=location
        )

        if data:
            jobs = data.get("jobs", [])

    return render(
        request,
        "jobs/jooble_jobs.html",
        {
            "jobs": jobs,
            "keyword": keyword,
            "location": location,
        }
    )


def home(request):
    vacancies = Vacancy.objects.order_by(
        "-created_at"
    )[:5]

    articles = Article.objects.order_by(
        "-created_at"
    )[:5]

    return render(
        request,
        "jobs/home.html",
        {
            "vacancies": vacancies,
            "articles": articles,
        }
    )

def edit_article(request, id):

    article = get_object_or_404(
        Article,
        id=id
    )

    if request.method == "POST":

        form = ArticleForm(
            request.POST,
            instance=article
        )

        if form.is_valid():

            form.save()

            return redirect(
                "article_detail",
                id=article.id
            )

    else:

        form = ArticleForm(
            instance=article
        )

    return render(
        request,
        "jobs/edit_article.html",
        {
            "form": form,
            "article": article
        }
    )

def vacancies(request):

    search = request.GET.get(
        "search",
        ""
    )

    vacancies = Vacancy.objects.filter(
        is_active=True
    )

    if search:
        vacancies = vacancies.filter(
            Q(title__icontains=search)
            |
            Q(company__icontains=search)
            |
            Q(location__icontains=search)
        )

    return render(
        request,
        "jobs/vacancies.html",
        {
            "vacancies": vacancies,
            "search": search,
        }
    )

def delete_article(request, id):

    article = get_object_or_404(
        Article,
        id=id
    )

    if request.method == "POST":

        article.delete()

        return redirect(
            "articles"
        )

    return render(
        request,
        "jobs/delete_article.html",
        {
            "article": article
        }
    )

def vacancy_detail(request, id):
    vacancy = get_object_or_404(
        Vacancy,
        id=id
    )

    return render(
        request,
        "jobs/vacancy_detail.html",
        {
            "vacancy": vacancy
        }
    )


def articles(request):
    articles = Article.objects.order_by(
        "-created_at"
    )

    return render(
        request,
        "jobs/articles.html",
        {
            "articles": articles
        }
    )


def article_detail(request, id):
    article = get_object_or_404(
        Article,
        id=id
    )

    return render(
        request,
        "jobs/article_detail.html",
        {
            "article": article
        }
    )


def add_article(request):

    if request.method == "POST":

        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("articles")

    else:
        form = ArticleForm()

    return render(
        request,
        "jobs/add_article.html",
        {
            "form": form
        }
    )


def about(request):
    return render(
        request,
        "jobs/about.html"
    )

def vacancy_detail(request, id):
    vacancy = get_object_or_404(
        Vacancy,
        id=id
    )

    vacancy.views += 1
    vacancy.save()

    return render(
        request,
        "jobs/vacancy_detail.html",
        {
            "vacancy": vacancy
        }
    )