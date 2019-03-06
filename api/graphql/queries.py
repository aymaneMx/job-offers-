import graphene
from django.contrib.auth import get_user_model

from api.graphql.types import OfferType, UserType
from api.models import Offer

from django.db.models import Q


class Query(graphene.ObjectType):
    current_user = graphene.Field(UserType)
    offers = graphene.List(OfferType, search=graphene.String())
    users = graphene.List(UserType)

    def resolve_offers(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )
            return Offer.objects.filter(filter)

        return Offer.objects.all()

    def resolve_users(self, info, **kwargs):
        return get_user_model().objects.all()

    def resolve_current_user(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user
