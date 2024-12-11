from django.shortcuts import render, HttpResponse
from . models import * #naimportovanie všetkych modelov z models.py v tomto priecčinku

# Create your views here.
def index(request):
    studenti = Student.objects.all()
    return HttpResponse(studenti)
