from django.shortcuts import render
from amodrel.models import Topic 

from  amodrel.models import Heading

# Create your views here.
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')

def gallery(request):

    headings = Heading.objects.all()
    topics = Topic.objects.all()
    
    return render(request, 'gallery.html', {'headings':headings, 'topics':topics},)