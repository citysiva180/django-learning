from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
# Create your views here.

# This http function is a default function and it accepts string as a message parameter


def say_hello(request):
    query_set = Product.objects.all()

    for product in query_set:
        print(product)
    # pulling all objects,  get for getting all objectd and pull
    # Data comming through ORM is a Query SET
    # Evaluation happens on running a query set.
    # It happens on Iteration,or conversion into a list or access an individual element

    # QuerySets are Lazy. Remember, loading everything at a single shot will make things complicated.
    return render(request, 'hello.html', {"name": "Siva"})

# post creating this function, we could then add this in the urls
