from django.contrib.auth import get_user_model

from graphene_django.types import DjangoObjectType

from api.models import Offer


class OfferType(DjangoObjectType):
    class Meta:
        model = Offer


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

