import pytest


@pytest.mark.django_db
def test_create_offer(auth_client):
    """ test create an offer """

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


@pytest.mark.django_db
def test_delete_offer(auth_client):
    """ test delete an offer """

    # create offer and save the ID to delete it after
    response_create_offer = auth_client.mutation(
        'createOffer',
        arguments='title: "test", description: "test", skillsList: ["skill1", "skill2"]',
        payload='offer { id }'
    )
    assert response_create_offer.status_code == 200
    response_out = response_create_offer.json()['data']['createOffer']
    offer_id = response_out['offer']['id']

    # delete offer that we just create
    response = auth_client.mutation(
        'deleteOffer',
        arguments='id: {}'.format(offer_id),
        payload='done'
    )
    assert response.status_code == 200
    assert isinstance(response.json()['data']['deleteOffer'], dict)
    response_out = response.json()['data']['deleteOffer']
    assert response_out['done']


