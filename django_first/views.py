from django.shortcuts import render
from datetime import datetime
from .models import Article

"""
class Article:
    '''A class with articles'''
    def __init__(self, title, content):
        self.title = title
        self.content = content
"""

def index(request):
    context = {
        'current_date': datetime.now(),
        'title': 'Home'
    }

    return render(request, 'index.html', context)

def about(request):
    context = {
        'current_date': datetime.now(),
        'title':'About'
    }
    return render(request, 'about.html', context)
def news(request):
    articles = get_articles()
    context = {
        'article1':articles[0],
        'article2':articles[1],
        'article3':articles[2],
        'current_date': datetime.now(),
        'title': 'News'
    }
    return render(request, 'news.html', context)

def get_articles():
    result = Article.objects.all()
    
    """
    article1 = Article(
        title = 'Article 1',
        content = '''This is a multiline content
            where you can define multiple line of strings
            without any error'''
    )
    article2 = Article(
        title = 'Article 2',
        content = '''This is a multiline content
            where you can define multiple line of strings
            without any error'''
    )
    article3 = Article(
        title = 'Article 3',
        content = '''This is a multiline content
            where you can define multiple line of strings
            without any error'''
    )

    result.append(article1)
    result.append(article2)
    result.append(article3)
    """
    return result