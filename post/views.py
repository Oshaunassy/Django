from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def test_view(request):
    return HttpResponse('Hello, it is my project')

def main_view(reguest):
    if reguest.method == 'GET':
        return render(reguest, 'index.html')
    # elif reguest.method == 'POST':

def current_date(request):
    now = datetime.now()
    return HttpResponse(f"Current date and time: {now}")

def goodbye(request):
    return HttpResponse("Goodbye user!")
