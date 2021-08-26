import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN
from my_shop_app.models import Product


@pytest.mark.django_db
def test_list_products(api_client):
    url = reverse("products-list")
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_create_product_user(api_client):
    url = reverse("products-list")
    product = {
        'name': 'Bosh',
        'description': 'Coffe',
        'price': '1234',
    }
    resp = api_client.post(url, product)
    assert resp.status_code == HTTP_403_FORBIDDEN
    assert Product.objects.count() == 0


@pytest.mark.django_db
def test_create_product_admin(admin_client):
    url = reverse("products-list")
    product = {
        'name': 'Earnshaw',
        'description': 'Watch',
        'price': '1234',
    }
    resp = admin_client.post(url, product)
    assert resp.status_code == HTTP_201_CREATED
    resp_json = resp.json()
    assert Product.objects.count() == 1
    assert resp_json['name'] == 'Earnshaw'
    return resp_json


@pytest.mark.django_db
def test_update_user(api_client, admin_client):
    resp_json = test_create_product_admin(admin_client)
    url = reverse("products-detail", args=[resp_json["id"]])
    product = {
        'name': 'Bosh',
        'description': 'Coffe',
        'price': '1234',
    }
    resp = api_client.patch(url, product)
    assert resp.status_code == HTTP_403_FORBIDDEN
    assert resp_json["name"] == 'Bosh'


@pytest.mark.django_db
def test_update_admin(admin_client):
    resp_json = test_create_product_admin(admin_client)
    url = reverse("products-detail", args=[resp_json["id"]])
    product = {
        'name': 'Earnshaw',
        'description': 'Watch',
        'price': '1234',
    }
    resp = admin_client.patch(url, product)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json["name"] == 'Earnshaw'
