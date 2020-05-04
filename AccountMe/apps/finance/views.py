from rest_framework import viewsets
from . import models
from . import serializers
from . import filters


class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
    filterset_class = filters.AccountFilter


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    filterset_class = filters.TransactionFilter
