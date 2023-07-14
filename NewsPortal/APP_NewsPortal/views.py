from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import NewForm, ArticleForm
from .models import New, Article
from .filters import NewFilter, ArticleFilter

from datetime import datetime


class NewList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = New
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_pub'
    # queryset = Product.objects.filter(price__lt=150).order_by('name')
    # Указываем имя шаблона, в котором будут все инcтрукции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_pub'] = datetime.utcnow()
        return context


class NewDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = New
    # Используем другой шаблон — product.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'new'
    pk_url_kwarg = 'id'


class NewListSearch(ListView):
    model = New
    ordering = '-date_pub'
    template_name = 'news_search.html'
    context_object_name = 'news_search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewCreate(CreateView):
    form_class = NewForm
    model = New
    template_name = 'new_edit.html'

    def form_valid(self, form):
        new = form.save(commit=False)
        new.categoryType = 'NW'
        new.save()
        return super().form_valid(form)


class NewUpdate(UpdateView):
    form_class = NewForm
    model = New
    template_name = 'new_edit.html'


class NewDelete(DeleteView):
    model = New
    template_name = 'new_delete.html'
    success_url = reverse_lazy('new_list')


class ArticleList(ListView):
    model = Article
    ordering = '-date_pub'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_pub'] = datetime.utcnow()
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'
    pk_url_kwarg = 'id'


class ArticleListSearch(ListView):
    model = Article
    ordering = '-date_pub'
    template_name = 'articles_search.html'
    context_object_name = 'articles_search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ArticleFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticleCreate(CreateView):
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.categoryType = 'AR'
        article.save()
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'


class ArticleDelete(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
