from importlib.resources import contents
from django.shortcuts import render
from django.db.models import Q
from project_app.models import Post



def searchResult(request):
    if 'word' in request.GET:
        query = request.GET.get('word')
        post = Post.objects.order_by('-created_at').filter(
            Q(author__icontains=query) |
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    return render(request, 'searched.html', {'query':query, 'post':post})
