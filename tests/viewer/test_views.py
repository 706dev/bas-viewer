import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_content_list_view():
    instance1 = test_helpers.create_viewer_content()
    instance2 = test_helpers.create_viewer_content()
    client = Client()
    url = reverse("viewer_content_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_content_create_view():
    client = Client()
    url = reverse("viewer_content_create")
    data = {
        "specific_date": 0,
        "file": "aFile",
        "title": "text",
        "duration": 1.0,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_content_detail_view():
    client = Client()
    instance = test_helpers.create_viewer_content()
    url = reverse("viewer_content_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_content_update_view():
    client = Client()
    instance = test_helpers.create_viewer_content()
    url = reverse("viewer_content_update", args=[instance.pk, ])
    data = {
        "specific_date": 0,
        "file": "aFile",
        "title": "text",
        "duration": 1.0,
    }
    response = client.post(url, data)
    assert response.status_code == 302
