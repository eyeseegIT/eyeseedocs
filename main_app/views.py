from django.shortcuts import render
from .models import Antseg

# Create your views here.
def home(request):
  return render(request, 'home.html')

def antsegs_index(request):
  antsegs = Antseg.objects.all()
  return render(request, "antsegs/index.html", { "antsegs": antsegs })

def antsegs_detail(request, antseg_id):
  antseg = Antseg.objects.get(id=antseg_id)
  return render(request, "antsegs/detail.html", { "antseg": antseg})