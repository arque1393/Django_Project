# # User Authentication
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.authtoken.models import Token
from .serializer import Customer, CustomerSerializer, UserSearializer
from rest_framework import generics
from django.shortcuts import render
# from django.http import JsonResponse
# Create your views here.
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customer
from .serializer import CustomerSerializer


@api_view(["GET", "POST"])
def api_home(req):
    if req.method == "POST":
        serializer = CustomerSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            print(instance)
            return Response(serializer.data)
        return Response({"data": "not Found"})

    data = Customer.objects.all().first()
    data = CustomerSerializer(data).data

    return Response(data)


@api_view(["post"])
def signup(req):
    serializer = UserSearializer(data=req.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()

        token = Token.objects.create(user=user)
        print(token.key)
        data = serializer.data
        data["Authorization"] = token.key
        return Response(data)


@api_view(["get"])
def getUser(req):
    user = req.user
    print(user)
    # searializer = UserSearializer(user)
    # return Response(searializer.data)
    return Response({})


@api_view(["post"])
def signin(req):


class CustomerCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response(serializer.data)


custome_create_view = CustomerCreateAPIView.as_view()


class CustomerDetailAPIView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


custome_detail_view = CustomerDetailAPIView.as_view()

# from rest_framework.views import APIView
