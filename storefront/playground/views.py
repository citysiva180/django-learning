from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# This http function is a default function and it accepts string as a message parameter


def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {"name": "Siva"})

# post creating this function, we could then add this in the urls
