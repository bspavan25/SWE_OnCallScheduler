from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.IntegerField()
    name = models.CharField( max_length=200)
    skills = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Availability(models.Model):
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    number_of_hours = models.IntegerField()

    def __str__(self):
        return self.employee.name + " " + str(self.number_of_hours)

class Skills(models.Model):
    skill_id = models.IntegerField()
    skill_name = models.CharField(max_length=200)

    def __str__(self):
        return self.skill_name
