from django.conf.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path("show_data", show_data),
    path("show_cert", show_cert),
    path("show_data_1", show_data_1),
    path("search_roa", search_roa),
    path("search_cert", search_cert),
    path("search_auth", search_auth),
    path("search", search),
    path("search_1", search_1),
    path("show_rov", show_rov),
    path("search_rov", search_rov),
    path('show_link', show_link),
    path('show_content', show_content)
]