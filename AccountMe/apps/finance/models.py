from django.db import models


class Transaction(models.Model):
    """
    A class used to represent a financial transaction
    v0.1
    ...

    Attributes
    ----------
    date : models.DateTimeField
        the date of the transaction
    description : models.CharField(max_length=64)
        a description of the transactions
    debit : models.IntegerField
        the total debit of a transaction in cents
    credit : models.IntegerField
        the total credit of a transaction in cents
    account : models.ForeignKey('Account', on_delete=models.CASCADE)
        the account that the transaction belongs to

    Methods
    -------
    __str__(self)
        returns a string of the date, description, debit, credit
    """

    date: models.DateTimeField = models.DateTimeField()
    description: models.CharField = models.CharField(max_length=64)
    debit: models.IntegerField = models.IntegerField()
    credit: models.IntegerField = models.IntegerField()
    account: models.ForeignKey = models.ForeignKey('Account', on_delete=models.CASCADE)

    def __str__(self)->str:
        return f"{self.date} {self.description} {self.debit} {self.credit}"


class Account(models.Model):
    """
    A class to represent a financial account
    v0.1
    ...
    Attributes
    ----------
    name : models.CharField(max_length=32, null=False)
        the name of the account
    transactions : models.ManyToManyField('Transaction')
        all of the transactions of an account

    Methods
    -------
    __str__(self)
        returns the name of the account
    """

    name: models.CharField = models.CharField(max_length=32, null=False)
    # TODO add a foreign key field of a user

    def __str__(self)->str:
        return self.name
