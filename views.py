from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import status
from .serializer import notes_noteSerializers
from .models import notes_note
from rest_framework.response import Response
from datetime import timezone
import datetime
from django.db import IntegrityError

class notes_noteViewSet(ModelViewSet):
    queryset = notes_note.objects.all()
    serializer_class= notes_noteSerializers

    def create(self,request):
        null = True
        obj= notes_note()
        obj.title = request.POST.get('title')
        obj.descrpition = request.POST.get('description')
        obj.date_created = datetime.datetime.now()
        obj.save()
        return Response({"response ":"Note Entry Succesfull"},status=status.HTTP_201_CREATED)

