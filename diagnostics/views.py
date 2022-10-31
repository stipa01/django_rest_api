from django.shortcuts import render
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for task
from . import serializers
from . import models


# Create your views here.

@csrf_exempt
def diagnostics(request):
    """
    List all task snippets
    """
    if request.method == 'GET':
        # get all the tasks
        report_data = models.EvDiagnostic.objects.all()
        # serialize the task data
        serializer = serializers.EvDiagnosticSerializer(report_data, many=True)
        # return a Json response
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.EvDiagnosticSerializer(data=data)
        # check if the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def diagnostic_detail(request, pk):
    try:
        diagnostic = models.EvDiagnostic.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if request.method == 'PUT':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.EvDiagnosticSerializer(diagnostic, data=data)
        # check whether the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        # delete the task
        diagnostic.delete()
        # return a no content response.
        return HttpResponse(status=204)


@csrf_exempt
def trouble_codes(request):
    """
    List all task snippets
    """
    if request.method == 'GET':
        # get all the tasks
        report_data = models.TroubleCode.objects.all()
        # serialize the task data
        serializer = serializers.TroubleCodeSerializer(report_data, many=True, context={'request': request})
        # return a Json response
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.TroubleCodeSerializer(data=data, context={'request': request})
        # check if the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def trouble_code_detail(request, pk):
    try:
        # obtain the task with the passed id.
        code = models.TroubleCode.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if request.method == 'PUT':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.TroubleCodeSerializer(code, data=data, context={'request': request})
        # check whether the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        # delete the task
        code.delete()
        # return a no content response.
        return HttpResponse(status=204)


@csrf_exempt
def vehicles(request):
    """
    List all task snippets
    """
    if request.method == 'GET':
        # get all the tasks
        report_data = models.Vehicle.objects.all()
        # serialize the task data
        serializer = serializers.VehicleSerializer(report_data, many=True)
        # return a Json response
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.VehicleSerializer(data=data)
        # check if the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def vehicle_detail(request, pk):
    try:
        # obtain the task with the passed id.
        vehicle = models.Vehicle.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if request.method == 'PUT':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.VehicleSerializer(vehicle, data=data)
        # check whether the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        # delete the task
        vehicle.delete()
        # return a no content response.
        return HttpResponse(status=204)


@csrf_exempt
def maintenance_schedules(request):
    """
    List all task snippets
    """
    if request.method == 'GET':
        # get all the tasks
        report_data = models.MaintenanceSchedules.objects.all()
        # serialize the task data
        serializer = serializers.MaintenanceScheduleSerializer(report_data, many=True, context={'request': request})
        # return a Json response
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.MaintenanceScheduleSerializer(data=data, context={'request': request})
        vehicle = models.Vehicle.objects.get(pk=serializer.initial_data['vehicle_id'])
        service_center = models.ServiceCenters.objects.get(pk=serializer.initial_data['service_center'])
        # check if the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save(vehicle=vehicle, service_center=service_center)
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def maintenance_schedule_detail(request, pk):
    try:
        # obtain the task with the passed id.
        maintenance = models.MaintenanceSchedules.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if request.method == 'PUT':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.MaintenanceScheduleSerializer(maintenance, data=data, context={'request': request})
        # check whether the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        # delete the task
        maintenance.delete()
        # return a no content response.
        return HttpResponse(status=204)


@csrf_exempt
def service_centers(request):
    """
    List all task snippets
    """
    if request.method == 'GET':
        # get all the tasks
        report_data = models.ServiceCenters.objects.all()
        # serialize the task data
        serializer = serializers.ServiceCenterSerializer(report_data, many=True)
        # return a Json response
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.ServiceCenterSerializer(data=data)
        # check if the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def service_center_detail(request, pk):
    try:
        # obtain the task with the passed id.
        service_center = models.ServiceCenters.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if request.method == 'PUT':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.ServiceCenterSerializer(service_center, data=data)
        # check whether the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        # delete the task
        service_center.delete()
        # return a no content response.
        return HttpResponse(status=204)


@csrf_exempt
def ev_diagnostics(request):
    """
    List all task snippets
    """
    if request.method == 'GET':
        # get all the tasks
        report_data = models.EvDiagnostic.objects.all()
        # serialize the task data
        serializer = serializers.EvDiagnosticSerializer(report_data, many=True, context={'request': request})
        # return a Json response
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.EvDiagnosticSerializer(data=data, context={'request': request})
        vehicle = models.Vehicle.objects.get(pk=serializer.initial_data['vehicle_id'])
        # check if the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save(vehicle=vehicle)
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def ev_diagnostic_detail(request, pk):
    try:
        # obtain the task with the passed id.
        diagnostic = models.EvDiagnostic.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if request.method == 'PUT':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.EvDiagnosticSerializer(diagnostic, data=data, context={'request': request})
        # check whether the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        # delete the task
        diagnostic.delete()
        # return a no content response.
        return HttpResponse(status=204)


@csrf_exempt
def engine_diagnostics(request):
    """
    List all task snippets
    """
    if request.method == 'GET':
        # get all the tasks
        report_data = models.EngineDiagnostic.objects.all()
        # serialize the task data
        serializer = serializers.EngineDiagnosticSerializer(report_data, many=True, context={'request': request})
        # return a Json response
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.EngineDiagnosticSerializer(data=data, context={'request': request})
        vehicle = models.Vehicle.objects.get(pk=serializer.initial_data['vehicle_id'])
        # check if the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save(vehicle=vehicle)
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def engine_diagnostic_detail(request, pk):
    try:
        # obtain the task with the passed id.
        diagnostic = models.EngineDiagnostic.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if request.method == 'PUT':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = serializers.EngineDiagnosticSerializer(diagnostic, data=data, context={'request': request})
        # check whether the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        # delete the task
        diagnostic.delete()
        # return a no content response.
        return HttpResponse(status=204)
