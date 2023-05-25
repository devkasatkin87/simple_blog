from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForms
from django.core.mail import send_mail


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

    try:
        # Мы получаем объекты для желаемой страницы, вызывая метод page() класса Paginator.
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # если введен
        posts = paginator.page(1)
    except EmptyPage:
        # Мы получаем объекты для желаемой страницы, вызывая метод page() класса Paginator.
        # если указан не существующий номер страницы то вывести последнюю страницу
        posts = paginator.page(paginator.num_pages)
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


# # возращает отправленную форму и данные поста, которым нужно поделится через почту
# def post_share(request, post_id):
#     # извлекаем данные по идентификатору id
#     post = get_object_or_404(Post, id = post_id, status = Post.Status.PUBLISHED)
#     sent = False # флаг отправки письма
#     #проверка каким методом был выполнен запрос POST or GET
#     if request == 'POST':
#         # форма была передана на обработку
#         form = EmailPostForms(request.Post)
#         if form.is_valid():
#             # поля формы успешно прошли валидацию
#             cd = form.cleaned_data

#             #создаем абсолютный адрес поста для запроса
#             post_url = request.build_absolute_uri(post.get_absolute_url())
#             # создаем тему, тело сообщения извлекая валидированные данные из формы
#             subject = f"{cd['name']} recommends you read" f"{post.title}"
#             message = f"Read {post.title} at {post_url} \n\n" f"{cd['name']}\s comments: {cd['comments']}"

#             # отправить письмо
#             send_mail(subject, message, 'your_account@gmail.com', [cd['to']])
#             sent = True
#             print(sent)
#     else:
#         # отобразить пустую форму
#         form = EmailPostForm()

#     print(sent)


#     return render(request, 'blog/post/share.html', {
#         'post' : post,
#         'form' : form,
#         'sent' : sent
#     })
# возращает отправленную форму и данные поста, которым нужно поделится через почту
def post_share(request, post_id):
    # извлекаем данные поста по идентификатору id
    post = get_object_or_404(Post, id=post_id, \
                                   status=Post.Status.PUBLISHED)
    # флаг отправки письма
    sent = False

    #проверка каким методом был выполнен запрос POST or GET
    if request.method == 'POST':
        # форма была передана на обработку
        form = EmailPostForms(request.POST)
        if form.is_valid():
            # поля формы успешно прошли валидацию
            cd = form.cleaned_data
            #создаем абсолютный адрес поста для запроса
            post_url = request.build_absolute_uri(post.get_absolute_url())

            # создаем тему, тело сообщения извлекая валидированные данные из формы
            subject = f"{cd['name']} recommends you read " \
                      f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"

            # отправить письмо
            send_mail(subject, message, 'your_account@gmail.com', [cd['to']])
            
            sent = True

    else:
        form = EmailPostForms()
    return render(request, 'blog/post/share.html', {
        'post': post,
        'form': form,
        'sent': sent
    })


class PostListView(ListView):
    """
        Альтернативное представление списка постов
    
    """

    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
