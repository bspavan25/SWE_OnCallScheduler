from django.test import TestCase, Client
from django.urls import reverse
from scheduler.models import Employee, Availability, Skills
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')

    def test_home_1_GET(self):
        client = Client()

        # create the test employees
        Employee.objects.create(
            employee_id = 1001,
            name = 'TE1',
            skills = [1, 3]
        )
        Employee.objects.create(
            employee_id = 1002,
            name = 'TE2',
            skills = [2, 4]
        )
        Employee.objects.create(
            employee_id = 1003,
            name = 'TE3',
            skills = [4, 2]
        )
        Employee.objects.create(
            employee_id = 1004,
            name = 'TE4',
            skills = [3, 1]
        )
        Employee.objects.create(
            employee_id = 1005,
            name = 'TE5',
            skills = [1, 3, 4]
        )
        Employee.objects.create(
            employee_id = 1006,
            name = 'TE6',
            skills = [2]
        )
        Employee.objects.create(
            employee_id = 1007,
            name = 'TE7',
            skills = [4, 2, 3]
        )
        Employee.objects.create(
            employee_id = 1008,
            name = 'TE8',
            skills = [1]
        )

        Availability.objects.create(
            employee = Employee.objects.get(employee_id = 1001),
            number_of_hours = 12
        )
        Availability.objects.create(
            employee = Employee.objects.get(employee_id = 1002),
            number_of_hours = 12
        )
        Availability.objects.create(
            employee = Employee.objects.get(employee_id = 1003),
            number_of_hours = 12
        )
        Availability.objects.create(
            employee = Employee.objects.get(employee_id = 1004),
            number_of_hours = 8
        )
        Availability.objects.create(
            employee = Employee.objects.get(employee_id = 1005),
            number_of_hours = 12
        )
        Availability.objects.create(
            employee = Employee.objects.get(employee_id = 1006),
            number_of_hours = 8
        )
        Availability.objects.create(
            employee = Employee.objects.get(employee_id = 1007),
            number_of_hours = 8
        )
        Availability.objects.create(
            employee = Employee.objects.get(employee_id = 1008),
            number_of_hours = 12
        )
        
        response = client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_2_GET(self):
        client = Client()

        # create the test employees
        Employee.objects.create(
            employee_id = 1001,
            name = 'TE1',
            skills = [1, 3]
        )

        Availability.objects.create(
            employee = Employee.objects.get(employee_id = 1001),
            number_of_hours = 12
        )
        
        response = client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')