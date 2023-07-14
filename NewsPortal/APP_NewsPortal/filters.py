from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter
from .models import New, Article


class NewFilter(FilterSet):
    date_pub = DateTimeFilter(
        field_name='date_pub',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y - %m - %dT%H:%M',
            attrs={'type': 'datetime-local'}
        )
    )

    class Meta:
        model = New
        fields = [
            'title',
            'category'
        ]


class ArticleFilter(FilterSet):
    date_pub = DateTimeFilter(
        field_name='date_pub',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y - %m - %dT%H:%M',
            attrs={'type': 'datetime-local'}
        )
    )

    class Meta:
        model = Article
        fields = [
            'title',
            'category'
        ]
