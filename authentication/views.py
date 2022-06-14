from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from .serializers import AuthenticationSerializer


# Create your views here.

def index(request):
    return render(request, 'vue-test.html')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def is_user_authenticated(request):
    return JsonResponse({
        'active': request.user.is_active,
    })


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        # parse the incoming information
        data = JSONParser().parse(request)
        user_object = User.objects.get(email=data['email'])
        user = authenticate(username=user_object.username, password=data['password'])
        token = None
        # refresh = None
        if user is not None and user.is_active:
            login(request, user)
            try:
                token = Token.objects.get(user_id=user.id)

            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            authenticated = True
        else:
            authenticated = False
        return JsonResponse({
            'user': {
                'username': user_object.username,
                'email': user_object.email,
                'first_name': user_object.first_name,
                'last_name': user_object.last_name,
                'token': token.key,
                'authenticated': authenticated,
            },
        })
    else:
        return JsonResponse({
            'authenticated': False,
            'user': None
        })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({
        'authenticated': False,
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def get_user_details(request):
    return JsonResponse({
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    })


@csrf_exempt
def register(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        # instantiate with the serializer
        serializer = AuthenticationSerializer(data=data)
        # check if the sent information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    # user.first_name = 'Lennon'
    # user.last_name = 'Bruce'
    # user.save()
    return JsonResponse({'registered': False}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def update_profile(request):
    user = User.objects.get(username='john')
    user.set_password('new password')
    user.save()
    return JsonResponse({
        'profile_updated': True,
        'user': user
    })
