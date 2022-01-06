from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem
# from storefront.store.models import OrderItem
# Create your views here.

# This http function is a default function and it accepts string as a message parameter


def say_hello(request):
    # products with inventory < 10 and Price < 20
    # queryset = Product.objects.values(
    #     'id', 'title')  # helps in limiting the data
    queryset = Product.objects.filter(
        id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    return render(request, 'hello.html', {"name": "Siva", 'products': list(queryset)})

# post creating this function, we could then add this in the urls

# NOTES FOR RETIRVING OBJECTS

# pulling all objects,  get for getting all objectd and pull
# Data comming through ORM is a Query SET
# Evaluation happens on running a query set.
# It happens on Iteration,or conversion into a list or access an individual element
# QuerySets are Lazy. Remember, loading everything at a single shot will make things complicated
# queryset = Product.objects.all() Returns all the data in the table | This returns a Query Set
# queryset = Product.objects.get(pk=1) Returns a single product of the specified ID | It Returns an Object
# product = Product.objects.filter(pk=0).first()

# NOTES FOR FILTERING OBJECTS

# Comparison values
