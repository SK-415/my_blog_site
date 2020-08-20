from django.shortcuts import redirect, render

def redirect_blog_list(request):
    response = redirect('article:article_list')
    return response

def baidu_verify(request):
    return render(request, 'baidu_verify_W1nBs3ybAH.html')