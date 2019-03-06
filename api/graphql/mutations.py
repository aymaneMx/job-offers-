import graphene
from django.contrib.auth import get_user_model

from api.graphql.types import UserType, OfferType
from api.models import Offer


class CreateOffer(graphene.Mutation):
    offer = graphene.Field(OfferType)

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        skills_list = graphene.List(graphene.String)

    def mutate(self, info, **kwargs):
        user = info.context.user

        if user.is_anonymous:
            raise Exception('You must be logged to create an offer !')

        offer = Offer(
            **kwargs,
            user=user
        )

        offer.save()

        return CreateOffer(offer=offer)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_offer = CreateOffer.Field()
    create_user = CreateUser.Field()
