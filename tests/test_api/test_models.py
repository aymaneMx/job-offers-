import pytest

from tests.test_api.factories import OfferFactory, UserFactory


@pytest.mark.django_db
def test_user_model():
    """ Test user model """

    # create user model instance
    user = UserFactory(
        username="username1",
        email="email@obytes.com",
        password="password123"
    )

    assert user.username == "username1"
    assert user.email == "email@obytes.com"


@pytest.mark.django_db
def test_offer_model():
    """ Test offer model """

    user = UserFactory(
        username="username1",
        email="email@obytes.com",
        password="password123"
    )

    offer = OfferFactory(
        title='title test',
        description='description description description description description ',
        skills_list=['django', 'graphql'],
        user=user
    )

    assert offer.title == 'title test'
    assert offer.description == 'description description description description description '
    assert offer.skills_list == ['django', 'graphql']

    assert str(offer) == 'title test'

    assert offer.user == user
    assert offer.user.username == "username1"
