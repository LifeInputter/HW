from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *

# Create your views here.
def blog_about_games(request):
    posts = Post.objects.all().order_by('-created_at') #сортировка в порядке от свежих постов к старым
    elements_per_page = request.GET.get('elements_per_page', 3)
    paginator = Paginator(posts, per_page=elements_per_page)
    page_numb = request.GET.get('page')
    try:
        page_posts = paginator.page(page_numb)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    context = {
        'page_posts': page_posts,
        'elements_per_page': elements_per_page
    }
    return render(request, 'index.html', context)