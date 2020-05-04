from django.db import models


class Transaction(models.Model):
    """
    A class used to represent a financial transaction
    ...

    Attributes
    ----------
    date : models.DateField
        the date of the transaction
    description : models.CharField(max_length=64)
        a description of the transactions
    amount : models.IntegerField
        the amount of credit/debit of a transaction (in cents)
    account : models.ForeignKey('Account', on_delete=models.CASCADE)
        the account that the transaction belongs to

    Methods
    -------
    __str__(self)
        returns a string of the date, description, debit, credit
    """

    date: models.DateField = models.DateField()
    description: models.CharField = models.CharField(max_length=64)
    amount: models.IntegerField = models.IntegerField()
    account: models.ForeignKey = models.ForeignKey('Account', on_delete=models.CASCADE)

    def __str__(self)->str:
        return f"AccountID #{account} '{self.description}' {self.amount}"


class Account(models.Model):
    """
    A class to represent a financial account
    ...
    Attributes
    ----------
    name : models.CharField(max_length=32, null=False)
        the name of the account

    Methods
    -------
    __str__(self)
        returns the name of the account
    """

    name: models.CharField = models.CharField(max_length=32)
    # TODO add a foreign key field of a user

    def __str__(self)->str:
        return self.name
