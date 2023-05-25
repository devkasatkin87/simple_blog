from django.urls import path
from . import views

app_name = 'blog'

# определяет шаблон построения url(маршруты)
urlpatterns = [
    # post views
    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_details, name='post_details'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]