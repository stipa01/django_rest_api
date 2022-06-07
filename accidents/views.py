from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for task
from rest_framework.permissions import IsAuthenticated

from .serializers import AccidentSerializer
# Task model
from .models import Accident


# Create your views here.


class AccidentView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # get all the tasks
        report_data = Accident.objects.all()
        # serialize the task data
        serializer = AccidentSerializer(report_data, many=True)
        # return a Json response
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def accidents(request):
    """
    List all task snippets
    """
    if request.method == 'GET':
        # get all the tasks
        report_data = Accident.objects.all()
        # serialize the task data
        serializer = AccidentSerializer(report_data, many=True)
        # return a Json response
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = AccidentSerializer(data=data)
        # check if the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def accident_detail(request, pk):
    try:
        # obtain the task with the passed id.
        accident = Accident.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if request.method == 'PUT':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = AccidentSerializer(accident, data=data)
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
        accident.delete()
        # return a no content response.
        return HttpResponse(status=204)
