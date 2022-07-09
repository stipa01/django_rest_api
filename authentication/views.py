from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import logout
from .serializers import MyTokenObtainPairSerializer, AuthenticationSerializer
from .models import MyUser, Profile


# Create your views here.

def index(request):
    return render(request, 'vue-test.html')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def is_user_authenticated(request):
    return JsonResponse({
        'active': request.user.is_active,
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


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def register(request):
    data = JSONParser().parse(request)
    # instantiate with the serializer
    serializer = AuthenticationSerializer(data=data)
    # check if the sent information is okay
    if serializer.is_valid():
        # if okay, save it on the database
        user = MyUser.objects.create(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            first_name=serializer.validated_data['first_name'],
            last_name=serializer.validated_data['last_name']
        )

        user.set_password(serializer.validated_data['password'])
        user.save()
        profile = Profile(user=user, phone=data['phone'])
        profile.save()
        # provide a Json Response with the data that was saved
        return JsonResponse(serializer.data, status=201)
    # provide a Json Response with the necessary error information
    else:
        return JsonResponse(serializer.errors, status=400)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def update_profile(request):
    user = MyUser.objects.get(username='john')
    user.set_password('new password')
    user.save()
    return JsonResponse({
        'profile_updated': True,
        'user': user
    })
