from django.test import TestCase
from scheduler.models import Employee, Availability, Skills


class TestModels(TestCase):
    def testEmployee(self):
        Employee.objects.create(
            employee_id = 1001,
            name = 'TE1',
            skills = [1, 3]
        )
        self.assertEquals(str(Employee.objects.get(employee_id=1001).__str__), '<bound method Employee.__str__ of <Employee: TE1>>')
    
    def testAvailability(self):
        Employee.objects.create(
            employee_id = 1001,
            name = 'TE1',
            skills = [1, 3]
        )
        Availability.objects.create(
            employee = Employee.objects.get(employee_id = 1001),
            number_of_hours = 12
        )
        self.assertEquals(str(Availability.objects.get(employee = Employee.objects.get(employee_id = 1001)).__str__), '<bound method Availability.__str__ of <Availability: TE1 12>>')

    def testSkill(self):
        Skills.objects.create(
            skill_id=1,
            skill_name='Django'
        )
        self.assertEquals(str(Skills.objects.get(skill_id=1).__str__), '<bound method Skills.__str__ of <Skills: Django>>')
