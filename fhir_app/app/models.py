from django.db import models
from rest_framework import serializers

# Create your models here.

class Patients(models.Model):
    patient_id = models.CharField(unique=True,null=False,default=None)
    active = models.BooleanField(default=False)
    family_name = models.CharField(max_length=100,null=True, blank=True)
    given_name = models.CharField(max_length=100,null=True, blank=True)
    work_phone =  models.CharField(max_length=15,null=True, blank=True)
    mobile_phone = models.CharField(max_length=15,null=True, blank=True)
    gender = models.CharField(max_length=30,null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = 'Patients'

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

class Observations(models.Model):
    observation_id = models.CharField(unique=True,null=False,default=None)
    source = models.CharField(max_length=100,null=True, blank=True)
    category = models.CharField(max_length=1000,null=True, blank=True)
    code = models.CharField(max_length=1000,null=True, blank=True)
  
    
    class Meta:
        db_table = 'Observations'

class ObservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observations
        fields = '__all__'


 