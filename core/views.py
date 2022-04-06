from django.shortcuts import render, HttpResponse

# Create your views here.

def indexcore(request):
    return HttpResponse("this is the equivalent of @core.route('/')!")