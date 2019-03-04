import pytest


@pytest.mark.django_db
def test_create_offer(auth_client):

    # auth_client.user.points = 100
    # auth_client.user.save()

    response = auth_client.mutation(
        'CreateOffer',
        arguments='title: "test", description: "test"',
        payload='offer { id title description user { id username }}'
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_user(auth_client):

    response = auth_client.mutation(
        'CreateUser',
        arguments='username: "test", email: "email", password: "test"',
        payload='user { id username email password }'
    )
    assert response.status_code == 200
