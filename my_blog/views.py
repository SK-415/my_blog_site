from django.shortcuts import redirect

def redirect_blog_list(request):
    response = redirect('article:article_list')
    return response