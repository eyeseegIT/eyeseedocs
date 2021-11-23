from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Antseg, Postseg, AntsegPhoto, PostsegPhoto
from django.views.generic import ListView, DetailView
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'eye-see-docs'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def antsegs_index(request):
  antsegs = Antseg.objects.all()
  return render(request, "antsegs/index.html", { "antsegs": antsegs })

def antsegs_detail(request, antseg_id):
  antseg = Antseg.objects.get(id=antseg_id)
  return render(request, "antsegs/detail.html", { "antseg": antseg})

class AntsegCreate(CreateView):
  model = Antseg
  fields = "__all__"
  success_url = "/antsegs/"

class AntsegUpdate(UpdateView):
  model = Antseg
  fields= "__all__"

class AntsegDelete(DeleteView):
  model = Antseg
  success_url = "/antsegs/"

class PostsegCreate(CreateView):
  model = Postseg
  fields = "__all__"

class PostsegList(ListView):
  model = Postseg

class PostsegDetail(DetailView):
  model = Postseg

class PostsegUpdate(UpdateView):
  model = Postseg
  fields= "__all__"

class PostsegDelete(DeleteView):
  model = Postseg
  success_url = "/postsegs/"

def add_antseg_photo(request, antseg_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = AntsegPhoto(url=url, antseg_id=antseg_id)
      antseg_photo = Photo.objects.filter(antseg_id=antseg_id)
      if antseg_photo.first():
        antseg_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('antsegs_detail', antseg_id=antseg_id)

def add_postseg_photo(request, postseg_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = PostsegPhoto(url=url, postseg_id=postseg_id)
      postseg_photo = Photo.objects.filter(postseg_id=postseg_id)
      if postseg_photo.first():
        postseg_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('postseg_detail', postseg_id=postseg_id)