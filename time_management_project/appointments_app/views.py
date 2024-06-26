from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from appointments_app.models import Appointment, Address
from datetime import datetime

# TODO: w3schools django add master template

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def appointments(request):
    appointments = Appointment.objects.all().values()
    template = loader.get_template('appointments.html')
    context = {
        'appointments': appointments
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    appointment = Appointment.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        "appointment" : appointment
    }
    return HttpResponse(template.render(context, request))

def add_appointment(request):
    address = Address(country="AT", city="Telfs", postal_code="6410", street="Weißenbachgasse", number="1")
    if not address in Address.objects.all():
        address.save()
    appointment = Appointment(name="Test", description="", start=datetime.now(), end=datetime.now(), address=address) 
    if not appointment in Appointment.objects.all():
        appointment.save()
    print(Appointment.objects.all().values())
    return HttpResponse("Add appointment")

def edit_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    template = loader.get_templates('edit.html')
    context = {
        'id':id,
        'name':appointment.name,
        'description':appointment.description,
        'start':appointment.start,
        'end':appointment.end,
        'address':appointment.address

    }
    print(appointment)
    #appointment.save()
    return HttpResponse(template.render(context, request))

def delete_appointment(request):
    return HttpResponse("Delete appointment")