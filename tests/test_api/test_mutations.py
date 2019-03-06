import pytest


@pytest.mark.django_db
def test_create_offer(auth_client):

    # auth_client.user.points = 100
    # auth_client.user.save()

    response = auth_client.mutation(
        'createOffer',
        arguments='title: "test", description: "test", skillsList: ["skill1", "skill2"]',
        payload='offer { id title description skillsList user { id username }}'
    )
    assert response.status_code == 200

    assert isinstance(response.json()['data']['createOffer'], dict)
    response_out = response.json()['data']['createOffer']
    assert response_out['offer']['id'] is not None
    assert response_out['offer']['title'] == 'test'
    assert response_out['offer']['description'] == 'test'
    assert response_out['offer']['skillsList'] == ["skill1", "skill2"]
    assert response_out['offer']['user']['id'] == str(auth_client.user.id)
    assert response_out['offer']['user']['username'] == auth_client.user.username

