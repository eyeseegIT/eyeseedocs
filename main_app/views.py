from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Antseg, Postseg, AntsegPhoto, PostsegPhoto
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'eye-see-docs'

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

@login_required
def antsegs_index(request):
  # antsegs = Antseg.objects.all()
  antsegs = Antseg.objects.filter(user=request.user)
  return render(request, "antsegs/index.html", { "antsegs": antsegs })

@login_required
def antsegs_detail(request, antseg_id):
  antseg = Antseg.objects.get(id=antseg_id)
  return render(request, "antsegs/detail.html", { "antseg": antseg})

class AntsegCreate(LoginRequiredMixin, CreateView):
  model = Antseg
  fields = ["diagnosis", "description"]
  
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class AntsegUpdate(LoginRequiredMixin, UpdateView):
  model = Antseg
  fields= ["diagnosis", "description"]

class AntsegDelete(LoginRequiredMixin, DeleteView):
  model = Antseg
  success_url = "/antsegs/"

class PostsegCreate(LoginRequiredMixin, CreateView):
  model = Postseg
  fields = ["diagnosis", "description"]

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class PostsegList(LoginRequiredMixin, ListView):
  model = Postseg

  def get_queryset(self):
    return self.model.objects.filter(user=self.request.user)

class PostsegDetail(LoginRequiredMixin, DetailView):
  model = Postseg

class PostsegUpdate(LoginRequiredMixin, UpdateView):
  model = Postseg
  fields= ["diagnosis", "description"]

class PostsegDelete(LoginRequiredMixin, DeleteView):
  model = Postseg
  success_url = "/postsegs/"

@login_required
def add_antseg_photo(request, antseg_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = AntsegPhoto(url=url, antseg_id=antseg_id)
      antseg_photo = AntsegPhoto.objects.filter(antseg_id=antseg_id)
      if antseg_photo.first():
        antseg_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('antsegs_detail', antseg_id=antseg_id)

@login_required
def add_postseg_photo(request, postseg_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = PostsegPhoto(url=url, postseg_id=postseg_id)
      postseg_photo = PostsegPhoto.objects.filter(postseg_id=postseg_id)
      if postseg_photo.first():
        postseg_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('postsegs_detail', pk=postseg_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('antsegs_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)


