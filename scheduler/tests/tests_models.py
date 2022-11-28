from django.test import TestCase
from scheduler.models import Employee, Availability, Skills


class TestModels(TestCase):
    def setUp(self):
        Employee.objects.create(
            employee_id = 1001,
            name = 'TE1',
            skills = [1, 3]
        )
        
    # def testEmployee(self):
    #     self.assertEquals(len(Employee.objects.__len__), 1)
