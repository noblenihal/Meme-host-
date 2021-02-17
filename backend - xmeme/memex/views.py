from django import http
from django.db.models import fields
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.views.generic import View
import json
from memex.models import memeinfo
from django.http import request
from django.core.serializers.json import Serializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MemeSerializer



# Create your views here.

@csrf_exempt 
@api_view(['GET', 'POST'])                     
def MemeList(request):
    if request.method == 'GET':
        MAX_OBJECTS = 100
        memes = memeinfo.objects.all().order_by('-id')[:MAX_OBJECTS]
        memedata = MemeSerializer(memes, many=True)   
        return Response(memedata.data)
    
    elif request.method == 'POST':
        payload = json.load(request)
        name = payload['name']
        caption = payload['caption']
        url = payload['url']

        if memeinfo.objects.filter(name = name, caption = caption, url = url).exists():
            return HttpResponse('Error : This Meme already exists', status=409)

        meme = memeinfo(name = name, caption = caption, url = url)
        
        try:
            meme.save()
            response  = {"id": str(meme.pk)} 
            print(response)                              #    ------ REMOVE THIS -----
        except:
            response  = {'Error':"There is some error"} 

        return JsonResponse(response , status=201)

                

@api_view(['GET','PATCH'])
def get_meme(request,id):
    if request.method == 'GET':
        meme = get_object_or_404(memeinfo,id =id)
        memedata = MemeSerializer(meme)
        return Response(memedata.data)

    elif request.method == 'PATCH':
        meme = get_object_or_404(memeinfo,id =id)
        payload = json.load(request)
        meme.caption = payload['caption']
        meme.url = payload['url']
        try:
            meme.save(update_fields=['caption','url'])
            return HttpResponse(status=204)
        except:
            return HttpResponse("There was some error")
    
 
        