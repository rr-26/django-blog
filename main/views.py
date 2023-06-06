from django.shortcuts import render
from main import models


# Create your views here.
def index(request):

    latest_articles = models.Article.objects.all().order_by('-createdAt')[:10]
    context = {
        "latest_articles": latest_articles
    }

    return render(request, 'main/index.html', context)
