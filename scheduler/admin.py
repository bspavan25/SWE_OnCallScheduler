from django.contrib import admin
from scheduler.models import Employee, Availability, Skills

# Register your models here.

class AdminEmployee(admin.ModelAdmin):
    model = Employee
    list_display = ('id', 'name', 'skills')

class AdminAvailability(admin.ModelAdmin):
    model = Availability
    list_display = ('id','employee', 'number_of_hours')

class AdminSkills(admin.ModelAdmin):
    model = Skills
    list_display = ('id','skill_name')

admin.site.register(Employee, AdminEmployee)
admin.site.register(Availability, AdminAvailability)
admin.site.register(Skills, AdminSkills)
