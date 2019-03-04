import factory
from django.contrib.auth import get_user_model

from api.models import Offer


class UserFactory(factory.DjangoModelFactory):
    """
        Define User Factory
    """
    class Meta:
        model = get_user_model()


class OfferFactory(factory.DjangoModelFactory):
    """
        Define Offer Factory
    """
    class Meta:
        model = Offer

    # Relationships
    user = factory.SubFactory(UserFactory)
