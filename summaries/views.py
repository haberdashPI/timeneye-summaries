from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import redirect
from datetime import datetime, timedelta

import requests
from base64 import b64encode
import json

def index(request):
    return render(request, 'summaries/login.html')

clientId = "a7771414caca7f457a85a8f2fd63c1b7"
with open('secret','r') as file:
    secret = file.read()

# TODO: store tokens by user in a database and refresh them as needed
@require_GET
def authenticate(request):
    auth_code = request.GET['code']
    url = "https://track.timeneye.com/api/3/token/"+clientId+"/"+auth_code
    encoding = b64encode((clientId+":"+secret).encode('ascii'))
    headers = {'Authorization': b'Basic '+encoding}
    response = requests.request("GET",url,headers=headers)
    resp = json.loads(response.content)

    return redirect('/timeneye/summary/'+resp["accessToken"])

def summary(request,token):
    oneweek = datetime.today() - timedelta(weeks=1)
    onemonth = datetime.today() - timedelta(days=30)

    url = "https://track.timeneye.com/api/3/entries"
    headers = {'Bearer': token}
    query = {"dateFrom": oneweek.strftime('%Y-%m-%d')}
    response = requests.request("GET",url,headers=headers)
    resp = json.loads(response.content)

    return HttpResponse(response.content)


