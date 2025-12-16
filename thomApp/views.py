from django.shortcuts import render,HttpResponse
import requests
from django.http import JsonResponse



def home(request):
    # return render(request,'thomApp/index.html')
    thom='battambang'
    API_Key='3aef1df689e335c34f01af97a72a88f4'
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    response=requests.get(url.format(thom,API_Key)).json()
    
    return JsonResponse(response)
    # return HttpResponse(response['name'])
def test(request):
    return HttpResponse("My Test Sitha")
