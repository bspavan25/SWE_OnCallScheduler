from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = 'OnCall Scheduler'                   
admin.site.index_title = 'Scheduler Administration'                 
admin.site.site_title = 'OnCall Scheduler'

urlpatterns= [
    path('', views.home, name="home")
]