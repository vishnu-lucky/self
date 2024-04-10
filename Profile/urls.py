from django.urls import path
from . import views

urlpatterns = [
    	path('',views.home,name="home"),
        path('proj/',views.project,name="project"),
        path('contact/',views.contact,name="contact"),


]
