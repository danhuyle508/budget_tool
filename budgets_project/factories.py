import factory
from django.contrib.auth.models import User
from board.models import 

class UserFactory(factory.django.DjangoModelFactory):
    """Create a test user for writing tests."""

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

class BudgetFactory(factory.django.DjangoModelFactory):
    """Create a test category for budget"""

    class Meta:
        model = Budget

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('word')
    amount = factory.Faker('')
    description = factory.Faker('paragraph')

class TransactionFactory(factory.django.DjangoModelFactory):
    """Create a test category for transaction"""

    class Meta:
        model = Transaction

    assigned_to = factory.SubFactory(UserFactory)
    budget = factory.SubFactory(BudgetFactory)
    amount = factory.Faker('')
    description = factory.Faker('paragraph')
    
