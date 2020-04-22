from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Transaction, Account
from .serializers import AccountSerializer, TransactionSerializer
from datetime import datetime
import json


class BaseViewTest(APITestCase):

    client: APIClient = APIClient()

    @staticmethod
    def create_account(name)->None:
        if name:
            Account.objects.create(name)

    @staticmethod
    def create_transaction(date, description, debit, credit, account)->None:
        Transaction.objects.create(
            date=date,
            description=description,
            debit=debit,
            credit=credit,
            account=account
        )

    @staticmethod
    def transaction_payload(date, description, debit, credit, account)->dict:
        return {
            'date': date,
            'description': description,
            'debit': debit,
            'credit': credit,
            'account': account
        }

    @staticmethod
    def account_payload(name) -> dict:
        return {
            'name': f'Account {name}'
        }

    def setup(self):
        for i in range(3):
            self.create_account(f'Bank Account #{i}')

        for i in range(10):
            self.create_transaction(
                date=datetime.now(),
                description=f'Transaction #{i}',
                debit=i*72,
                credit=0,
                account=1
            )


class FinanceTesting(BaseViewTest):

    """
    def test_post_accounts(self)->None:
        payload = self.post_account_payload(0)

        response = self.client.post(
            '/api/accounts/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_transactions(self)->None:
        payload = self.transaction_payload(
            date=str(datetime.now()),
            description='Transaction',
            debit=72,
            credit=0,
            account=1
        )

        response = self.client.post(
            '/api/transactions/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    """

    def test_get_all_accounts(self)->None:
        response = self.client.get('/api/accounts/')
        serializer = AccountSerializer(Account.objects.all(), many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_transactions(self)->None:
        response = self.client.get('/api/transactions/')
        serializer = TransactionSerializer(Transaction.objects.all(), many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
