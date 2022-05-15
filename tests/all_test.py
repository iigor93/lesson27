import pytest

from tests.factories import AdFactory, SelectionFactory


@pytest.mark.django_db
def test_get_request_list(client):
    """Получение списка объявлений"""
    
    ad = AdFactory.create()
    expected_data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                    {
                        "id": ad.pk,
                        "author": None,
                        "category": None,
                        "is_published": False,
                        "name": "new_ads_min_len_10",
                        "price": 44,
                        "description": None,
                        "image": None
                    }
                ]
                }

    response = client.get("/ads/")
    
    assert response.status_code == 200
    assert response.data == expected_data
    
    
@pytest.mark.django_db
def test_get_request_one(client, get_token):
    """Получение одного объявления"""
    
    ad = AdFactory.create()
    response = client.get(f"/ads/{ad.pk}/", format='json', HTTP_AUTHORIZATION='Bearer ' + get_token)

    expected_data = {
        "id": ad.pk,
        "author": None,
        "category": None,
        "is_published": False,
        "name": "new_ads_min_len_10",
        "price": 44,
        "description": None,
        "image": None
    }
    
    assert response.status_code == 200
    assert response.data == expected_data
    
    
@pytest.mark.django_db
def test_post_ads(client, get_token):
    """Создание объявления"""
    ad = AdFactory.create()
    data = {
        "name": "new_ads_min_len_10_2",
        "price": 44
        }
    
    expected_data = {
        "id": int(ad.pk + 1),
        "author": None,
        "category": None,
        "is_published": False,
        "name": "new_ads_min_len_10_2",
        "price": 44,
        "description": None,
        "image": None
        }
    
    response = client.post(f"/ads/create/", data=data, format='json', HTTP_AUTHORIZATION='Bearer ' + get_token)
    
    assert response.status_code == 201
    assert response.data == expected_data
    

@pytest.mark.django_db
def test_post_selection(client, get_token):
    """Создание подборки"""
    ad = AdFactory.create()
    selection = SelectionFactory.create()
    selection.ads.add(ad)
    data = {
            "name": "NewSelectionName",
            "owner": 1,
            "ads": [1]
            }
    
    expected_data = {
                    "id": int(selection.pk + 1),
                    "name": "NewSelectionName",
                    "owner": 1,
                    "ads": [1]
                    }
    
    response = client.post(f"/selection/create/", data=data, format='json', HTTP_AUTHORIZATION='Bearer ' + get_token)
    
    assert response.status_code == 201
    assert response.data == expected_data
   
