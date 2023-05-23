from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator


# Функция возращает все посты со статусом published и передает их по указанному URL
def post_list(request):
    post_list = Post.published.all()

    # создаем объект класса Paginator с количеством 3 постов на страницу
    paginator = Paginator(post_list, 3)
    # Мы извлекаем HTTP GET-параметр page и сохраняем его в переменной page_number. 
    # Этот параметр содержит запрошенный номер страницы. Если параметра page нет в GET-параметрах запроса, 
    # то мы используем стандартное значение 1, чтобы загрузить первую страницу результатов.
    #page_number = request.GET.get('page', 1)
    page_number = request.GET.get('page', 1)
    # Мы получаем объекты для желаемой страницы, вызывая метод page() класса Paginator.
    posts = paginator.page(page_number)

    # Мы передаем номер страницы и объект posts в шаблон.
    return render(request, 'blog/post/list.html', {'posts': posts})


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
def post_details(request, year, month, day, post):

    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'blog/post/details.html', {'post': post})
