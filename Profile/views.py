from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
	return render(request,'home.html')

def project(request):
	return render(request,'project.html')

def contact(request):
	return render(request,'contact.html')
