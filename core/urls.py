
from django.contrib import admin
from django.urls import path
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fanlar/', fanlar, name='fanlar'),
    path('fanlar/<int:fan_id>', fan),
    path('fanlar/<int:fan_id>/delete', fan_delete),
    path('yonalishlar/', yonalishlar, name='yonalishlar'),
    path('yonalishlar/<int:yonalish_id>', yonalish_confirm),
    path('yonalishalr/<int:yonalish_id>/delete', yonalish_delete),
    path('ustozlar/', ustozlar, name='ustozlar'),
    path('ustozlar/<int:ustoz_id>/', ustoz_confirm),
    path('ustozlar/<int:ustoz_id>/delete', ustoz_delete),
]
