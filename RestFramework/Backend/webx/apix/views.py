from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def api_home(req):
    data = {"message": "I am great!!"}
    return JsonResponse(data)
