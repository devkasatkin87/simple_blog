from django.urls import path
from . import views

app_name = 'blog'

# определяет шаблон построения url(маршруты)
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_details, name='post_details'),
]