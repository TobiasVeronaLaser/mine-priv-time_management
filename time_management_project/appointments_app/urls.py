from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/details/<int:id>', views.details, name='details'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('edit_appointment/', views.edit_appointment, name='edit_appointment'),

]