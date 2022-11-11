from django.urls import path
from .views import api_home, custome_detail_view, custome_create_view  # , api_login
urlpatterns = [
    path('', api_home),    # Domainname.com/
    # path('login', api_login),    # Domainname.com/
    path('<int:pk>/', custome_detail_view),    # Domainname.com/
    path('create/', custome_create_view),    # Domainname.com/


]
