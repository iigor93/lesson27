import pytest


@pytest.fixture()
@pytest.mark.django_db
def get_token(client, django_user_model):
    username = 'igor'
    password = 'igor'
    is_staff = True
    
    django_user_model.objects.create_user(username=username, password=password, is_staff=is_staff)
    response = client.post("/user/token/", {"username": username, "password": password}, format='json')
    
    return response.data['access']
