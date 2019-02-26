import graphene
from django.contrib.auth import get_user_model

from api.graphql.types import OfferType, UserType
from api.models import Offer


class Query(graphene.ObjectType):
    current_user = graphene.Field(UserType)
    all_offers = graphene.List(OfferType)
    all_users = graphene.List(UserType)

    def resolve_all_offers(self, info, **kwargs):
        return Offer.objects.all()

    def resolve_all_users(self, info, **kwargs):
        return get_user_model().objects.all()

    def resolve_current_user(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user
