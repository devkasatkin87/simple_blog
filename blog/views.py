from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

# Функция возращает все посты со статусом published и передает их по указанному URL 
def post_list(request):
    posts = Post.published.all()
    
    return render(
        request, 
        'blog/post/list.html',
        {'posts' : posts}
        )

# # Возвражает пост с переданным Id по указанному Url, если не находит прокидывает ошибку Http404 
# def post_details(request, id):
    
#     try:
#         post = Post.published.get(id = id)
#     except Post.DoesNotExist:
#         raise Http404("Post not found!")
     
#     return render(
#          request, 
#          'blog/post/details.html',
#          {'post' : post}
#          )
    
# Возвражает пост с переданным Id по указанному Url, если не находит прокидывает ошибку Http404 
def post_details(request, id):
    
    post = get_object_or_404(Post, id = id, status = Post.Status.PUBLISHED)
     
    return render(
         request, 
         'blog/post/details.html',
         {'post' : post}
         )