from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter, ChoiceFilter
from .models import Post, Category
from django.forms import DateTimeInput
from .resources import CATEGORIES


class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category_ps',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='Все категории',
    )
    added_after = DateTimeFilter(
        field_name='time_post',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'name_post': ['icontains'],
        }

