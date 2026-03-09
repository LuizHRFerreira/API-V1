import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_user_model() -> None:
    user = User.objects.create_user(
        email="user@example.com",
        password="12345678",
        full_name="Usuário Teste",
    )

    assert user.email == "user@example.com"
    assert user.full_name == "Usuário Teste"
    assert user.check_password("12345678")


@pytest.mark.django_db
def test_list_users(client) -> None:
    User.objects.create_user(
        email="list@example.com",
        password="12345678",
        full_name="Lista Teste",
    )

    response = client.get("/api/users/")

    assert response.status_code == 200
    assert response.json()[0]["email"] == "list@example.com"


@pytest.mark.django_db
def test_create_user_api(client) -> None:
    payload = {
        "email": "api@example.com",
        "full_name": "API Teste",
        "password": "12345678",
    }

    response = client.post("/api/users/", payload, content_type="application/json")

    assert response.status_code == 201
    assert response.json()["email"] == payload["email"]
    assert User.objects.filter(email=payload["email"]).exists()
