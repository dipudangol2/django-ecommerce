from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "shop/index.html")


def about(request):
    return HttpResponse("Index about")


def contact(request):
    return HttpResponse("Index Contact")


def tracker(request):
    return HttpResponse("Index Tracker")


def search(request):
    return HttpResponse("Index Search")


def prodView(request):
    return HttpResponse("Index ProductView")


def checkout(request):
    return HttpResponse("Index Checkout")
