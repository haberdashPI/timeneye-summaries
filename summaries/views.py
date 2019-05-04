from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET

import requests
from base64 import b64encode
import json

def index(request):
    return render(request, 'summaries/login.html')

clientId = "a7771414caca7f457a85a8f2fd63c1b7"
with open('secret','r') as file:
    secret = file.read()

@require_GET
def authenticate(request):
    auth_code = request.GET['code']
    url = "https://track.timeneye.com/api/3/token/"+clientId+"/"+auth_code
    encoding = b64encode((clientId+":"+secret).encode('ascii'))
    headers = {'Authorization': b'Basic '+encoding}
    response = requests.request("GET",url,headers=headers)
    resp = json.loads(response.content)

<<<<<<< Updated upstream
    return HttpResponse("Good job! Access token is "+resp["accessToken"])


=======
    return redirect('/timeneye/summary/'+resp["accessToken"])

def summary(request,token):
    return render(request, 'summaries/app.html')
>>>>>>> Stashed changes
