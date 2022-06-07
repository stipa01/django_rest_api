from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token


# Create your views here.

def index(request):
    return render(request, 'vue-test.html')


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
            # A backend authenticated the credentials
            login(request, user)
            # refresh = RefreshToken.for_user(user)
            try:
                token = Token.objects.get(user_id=user.id)

            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            authenticated = True
        else:
            # No backend authenticated the credentials
            authenticated = False
        return JsonResponse({
            'user': {
                'username': user_object.username,
                'email': user_object.email,
                'first_name': user_object.first_name,
                'last_name': user_object.last_name,
                'token': token.key,
                'authenticated': authenticated,
                # 'access_token': refresh.access_token,
                # 'refresh': refresh,
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
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.first_name = 'Lennon'
    user.last_name = 'Bruce'
    user.save()
    return JsonResponse({
        'registered': True,
        'user': user
    })


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
