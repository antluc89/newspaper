from django.urls import path
from .views import (PostsList, PostDetail, NewsSearch, NewsCreate, NewsEdit, NewsDelete, ArticleCreate,
                    ArticleEdit, ArticleDelete, subscriptions)

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', NewsSearch.as_view(), name='post_search'),
    path('create/', NewsCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('article/<int:pl>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]
