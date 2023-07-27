from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password, settings
User = get_user_model()
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.contrib.auth import authenticate, login
class RegistrationView(ModelViewSet):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


@csrf_exempt
def Login(request):
    if request.method == "GET":
        return JsonResponse({'data': "Enter Email and Password in Postman"})
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method is allowed!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if "email" not in request.POST or "password" not in request.POST:
        return JsonResponse({"error": "Missing Required fields need Email and Password"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    email = request.POST.get("email", None)
    password = request.POST.get("password", None)
    user = authenticate(email=email, password=password)
    if user is not None:
        login(request, user)
        # return render(request, "")
        return JsonResponse({"success": "User has been logged in"})
    return JsonResponse(
        {"errors": "Invalid credentials"},
        status=400,
    )
