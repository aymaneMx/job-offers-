import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_current_user_query(auth_client):

    response = auth_client.query(
        'currentUser',
        payload='id username'
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_users_query(auth_client):

    response = auth_client.query(
        'users',
        payload='id username email'
    )
    assert response.status_code == 200
    assert isinstance(response.json()['data']['users'], list)
    assert len(response.json()['data']['users']) == get_user_model().objects.count()
    assert response.json()['data']['users'][0]['id'] is not None
    assert response.json()['data']['users'][0]['username'] is not None
    assert response.json()['data']['users'][0]['email'] is not None
