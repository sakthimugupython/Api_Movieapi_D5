from django.shortcuts import render

from rest_framework import viewsets, filters
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.pagination import LimitOffsetPagination
import django_filters.rest_framework as django_filters

class MovieFilter(django_filters.FilterSet):
    release_date = django_filters.DateFromToRangeFilter()
    rating = django_filters.NumericRangeFilter()

    class Meta:
        model = Movie
        fields = ['genre', 'release_date', 'rating']

class MoviePagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    filter_backends = [django_filters.DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = MovieFilter
    ordering_fields = ['release_date', 'rating']
    ordering = ['-rating', 'release_date']  # Default: rating DESC, release_date ASC
