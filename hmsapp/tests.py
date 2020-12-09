from django.test import TestCase
from .models import Service
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse 
from .serializer import *

# Create your tests here.
class ServiceTestClass(TestCase):

    # Set up method
    def setUp(self):

        """Define the test client and other test variables."""

        self.new_service=Service(service_name='X-ray',service_cost=500,service_description='Xray test')
        
    def test_model_can_create_a_service(self):

        """Test the service model can create a service"""

        self.new_service.save()
        count = Service.objects.count()
        self.assertTrue(count == 1)

    # Testing  instance

    def test_instance(self):

        self.assertTrue(isinstance(self.new_service,Service))    


class ServiceViewTestCase(TestCase):
    """Test suite for the service model api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.service=Service.objects.create(service_name='X-ray',service_cost=500,service_description='test')
        self.service_data = {'service_name': 'Consultant','service_cost':1500,'service_description':'test'}
        

    def test_api_can_create_a_service(self):
        """Test the api can create a service."""
        response = self.client.post(
            reverse('service_create'),
            self.service_data,
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



    def test_api_can_get_all_service(self):
        """ Test the api can get all services """
        # get API response
        response = self.client.get(reverse('service_create'))
        # get data from db
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_api_can_get_a_service(self):
        """Test the api can get a given service."""
        
        response = self.client.get(
            reverse('service_update',
            kwargs={'pk': self.service.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.service)

    def test_api_can_update_service(self):
        """Test the api can update a given service."""
        change_service = {'service_name': 'Consultant','service_cost':500,'service_description':'test'}
        
        res = self.client.put(
            reverse('service_update', kwargs={'pk': self.service.id}),
            change_service, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_service(self):
        """Test the api can delete a service."""
        response = self.client.delete(
            reverse('service_update', kwargs={'pk': self.service.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)