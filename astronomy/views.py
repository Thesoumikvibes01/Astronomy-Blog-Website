from .models import Topic
from django.shortcuts import render

# Create your views here.
def index(request):
    topics=Topic.objects.all()
   
    return render(request,"index.html", {'topics': topics})