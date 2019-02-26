import graphene
from django.contrib.auth import get_user_model

from api.graphql.types import UserType
from api.models import Offer


class CreateOffer(graphene.Mutation):
    # offer = graphene.Field(OfferType)
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    skills_list = graphene.String()
    user = graphene.Field(UserType)

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        skills_list = graphene.String()

    def mutate(self, info, title, description, skills_list):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You must be logged to vote!')

        offer = Offer(
            title=title,
            description=description,
            skills_list=skills_list,
            user=user
        )

        offer.save()

        return CreateOffer(
            id=offer.id,
            title=offer.title,
            description=offer.description,
            skills_list=offer.skills_list,
            user=offer.user,
        )


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
