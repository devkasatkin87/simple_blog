from django.contrib import admin
from .models import Post


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