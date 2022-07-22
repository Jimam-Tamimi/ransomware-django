from django.urls import include, path
from api.views import *


urlpatterns = [
    path('victim/', victim),
]
