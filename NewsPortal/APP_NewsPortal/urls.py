from django.urls import path

from .views import NewList, NewDetail, NewListSearch, NewCreate, NewUpdate, NewDelete, ArticleList, ArticleDetail, \
    ArticleListSearch, ArticleCreate, ArticleUpdate, ArticleDelete, subscriptions

urlpatterns = [
    path('news/', NewList.as_view(), name='new_list'),
    path('news/<int:id>', NewDetail.as_view(), name='new_detail'),
    path('news/search/', NewListSearch.as_view(), name='news_search'),
    path('news/create/', NewCreate.as_view(), name='new_create'),
    path('news/<int:pk>/update/', NewUpdate.as_view(), name='new_update'),
    path('news/<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),
    path('articles/', ArticleList.as_view(), name='article_list'),
    path('articles/<int:id>', ArticleDetail.as_view(), name='article_detail'),
    path('articles/search/', ArticleListSearch.as_view(), name='articles_search'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    # path('categories/<int:pk>', CategoryListView(), name='category-list'),
]
