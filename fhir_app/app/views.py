from django.shortcuts import render
from django.db import transaction
# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Observations,Patients,PatientsSerializer,ObservationsSerializer
from fhir_app.settings import env
import json
from .utils import add_url_params
import requests


"""
POST:
This endpoint is used to fetch patient data from the FHIR server and store in the postgres database based on the search criteria given.
for example, it only patient id and family name is given, it will query based on patient id and family name only and store in db

"""
@api_view(['GET', 'POST'])
def patients(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            if body_unicode and json.loads(body_unicode):
                search_params = json.loads(body_unicode)
                request_url = add_url_params(env('FHIR_PATIENT_ROOT_URL'),search_params)
                res = requests.get(request_url)
                if res.status_code!=200:
                    return Response({"error":json.loads(res.text)})
                result=json.loads(res.text)
                with transaction.atomic():
                    load_patient_model_from_result_dict(result['entry'])
                return Response(result['entry'])
            else:
                return Response({"error": "No search params. Please enter atleast one search params"})
        except Exception as error:
            return Response({"An exception occurred:": error})
    
    
    if request.method == 'GET':
        res = Patients.objects.all()
        serialized = PatientsSerializer(res,many=True)
        return Response(serialized.data)

    return Response("Method not available")


"""
POST:
This endpoint is used to fetch observation data from the FHIR server and store in the postgres database based on the search criteria given.
for example, it only category and code is given, it will query based on category and code only and store in db

"""


@api_view(['GET', 'POST'])
def observations(request):
    try:
        if request.method == 'POST':
            body_unicode = request.body.decode('utf-8')
            if body_unicode and json.loads(body_unicode):
                search_params = json.loads(body_unicode)
                request_url = add_url_params(env('FHIR_OBSERVATION_ROOT_URL'),search_params)
                res = requests.get(request_url)
                if res.status_code!=200:
                    return Response({"error":json.loads(res.text)})
                result=json.loads(res.text)
                with transaction.atomic():
                    load_observation_model_from_result_dict(result['entry'])
                return Response(result['entry'])
            else:
                return Response({"error": "No search params. Please enter atleast one search params"})
    except Exception as error:
            return Response({"An exception occurred:": error})
    
    if request.method == 'GET':
        res = Observations.objects.all()
        serialized = ObservationsSerializer(res,many=True)
        return Response(serialized.data)
    return Response("Method not available")


def load_patient_model_from_result_dict(result):
    bulk_data = []
    for info in result:
        patient_info = info['resource']
        bulk_data.append(Patients(
                patient_id = patient_info.get('id'),
                active = patient_info.get("active") if  patient_info.get("active") else False,
                family_name = patient_info['name'][0]['family'],
                given_name = patient_info['name'][0]['given'][0], 
                work_phone=  patient_info['telecom'][0].get('work') if patient_info.get('telecom') else None,
                mobile_phone=  patient_info['telecom'][0].get('mobile') if patient_info.get('mobile') else None,
                gender= patient_info.get('gender'),
                birth_date= patient_info.get('birthDate'),
                address= patient_info.get('address')
      ))
    Patients.objects.bulk_create(bulk_data,ignore_conflicts=True)


def load_observation_model_from_result_dict(result):
    bulk_data = []
    for info in result:
        observation_info = info['resource']
        bulk_data.append(Observations(
                observation_id = observation_info.get('id'),
                source = observation_info.get('meta')['source'],
                category = observation_info.get('category'),
                code =  observation_info.get('subject')
        ))
    Observations.objects.bulk_create(bulk_data,ignore_conflicts=True)

    