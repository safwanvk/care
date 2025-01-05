from django.urls import reverse
from polyfactory.factories.pydantic_factory import ModelFactory
from rest_framework import status

from care.emr.resources.user.spec import UserCreateSpec
from care.utils.tests.base import CareAPITestBase


class UserFactory(ModelFactory[UserCreateSpec]):
    __model__ = UserCreateSpec


class UserTestCreate(CareAPITestBase):
    """
    Test cases for checking User Creation

    Tests should check if permission is checked when user is created, validations are also checked
    """

    def setUp(self):
        self.base_url = reverse("users-list")

    def generate_user_data(self, **kwargs):
        return UserFactory.build(email=self.fake.email(), meta={}, **kwargs)

    def test_create_user_unauthenticated(self):
        response = self.client.post(self.base_url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_empty_user_validation(self):
        user = self.create_user()
        self.client.force_authenticate(user=user)
        response = self.client.post(self.base_url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_authorization(self):
        user = self.create_user()
        organization = self.create_organization(org_type="govt")
        new_user = self.generate_user_data(geo_organization=organization.external_id)
        self.client.force_authenticate(user=user)
        response = self.client.post(self.base_url, new_user.dict(), format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
