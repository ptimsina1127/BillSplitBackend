from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
import json

from .models import Item
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def loginpage(request):
    template = loader.get_template("signup.html")
    return HttpResponse(template.render())

def insertData(request):
    item1 = Item(itemName ="Momo",itemPrice = 40,itemCategory="Food")
    item2 = Item(itemName ="Chowmein",itemPrice = 60,itemCategory="Food")

    item1.save()
    item2.save()
    return (HttpResponse("Item Saved"))

def listItems(request):
    result = Item.objects.all().values()
   # resultJson = json.dumps(result)
    jsonData = {
    "book": {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "published_year": 1979,
    "isbn": "978-0-330-25864-7",
    "language": "English"
  }
    }
    
    return JsonResponse(jsonData)