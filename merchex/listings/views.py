from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    listings = Listing.objects.all()
    return render(request, 
    'listings/hello.html',
    {'bands': bands,
    'listings': listings})


def about(request):
    return HttpResponse(
        "<h1>About</h1><p>This is a simple about page</p>"
    )
