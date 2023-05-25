from django.contrib import admin
from .models import Post
from .models import Comment


# добавить модель блога на сайт администрирования
# адаптируем админку под наши задачи добавляя поля, варианты поиска и фильтрации
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # отображаемые заголовки
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    # фыльтр по полям
    list_filter = ['status', 'created', 'publish', 'author']
    # осуществлять поиск по полям...
    search_fields = ['title', 'body']
    # автоматическое заполнение полей (заполяем slug при заполнении title)
    prepopulated_fields = {'slug': ('title', )}
    # отбор ассоциированных объектов по полю
    raw_id_fields = ['author']
    # навигационная ссылка для навигации по иеерархии дат
    date_hierarchy = 'publish'
    # по умолчанию посты упорядочены по полям...
    ordering = ['status', 'publish']


# добавить модель комментариев на сайт администрирования
# адаптируем админку комментариев под наши задачи в плане отображаемых полей, фильтра, поиска и др.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # отображаемые заголовки
    list_display = ['name', 'email', 'post', 'created', 'active']
    # фыльтр по полям
    list_filter = ['active', 'created', 'updated']
    # осуществлять поиск по полям...
    search_fields = ['name', 'email', 'body']