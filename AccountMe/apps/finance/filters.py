from django_filters import rest_framework as filters
from . import models


class AccountFilter(filters.FilterSet):
    class Meta:
        model = models.Account

        fields = [
            'name',
        ]


class TransactionFilter(filters.FilterSet):
    class Meta:
        model = models.Transaction

        fields = {
            'date': ['exact', 'range'],
            'account': ['exact'],
        }

        exclude = [
            'description',
            'amount',
        ]
