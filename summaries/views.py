from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET


def index(request):
    return render(request, 'summaries/login.html')

@require_GET
def authenticate(request):
    return HttpResponse("Good job! Access code is "+request.GET['code'])


