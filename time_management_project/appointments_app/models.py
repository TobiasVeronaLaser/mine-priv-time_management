from django.db import models

class Address(models.Model):
    country = models.CharField(max_length=7)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=7)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=7)

class Appointment(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
    start = models.DateTimeField()
    end = models.DateTimeField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Participant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Contact(models.Model):
    type = models.PositiveIntegerField()
    content = models.CharField(max_length=255)

# joined tables

class AppointmentParticipant(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE,)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE,)

class ParticipantContact(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE,)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,)