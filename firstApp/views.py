from django.shortcuts import render, reverse
from django.http import HttpResponse

# Create your views here.

app_name = 'firstApp'


def first_index(request):
    global app_name
    url = reverse('firstApp:firstIndex')
    name = "{% url 'name'%}"
    print(url)
    return render(request, '01_createApp.html', locals())
