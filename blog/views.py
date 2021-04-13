from django.shortcuts import render
from django.utils import timezone
from .models import Post

# blog/post_list.htmlテンプレート、引数を返す
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# render(テンプレートを組み合わせる)