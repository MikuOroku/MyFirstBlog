from django.shortcuts import render

# blog/post_list.htmlテンプレート、引数を返す
def post_list(request):
    return render(request, 'blog/post_list.html', {})

# render(テンプレートを組み合わせる)
