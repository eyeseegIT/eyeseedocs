from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Antseg(models.Model):
  diagnosis= models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.diagnosis

  def get_absolute_url(self):
    return reverse('antsegs_detail', kwargs={'antseg_id': self.id})

class Postseg(models.Model):
  diagnosis= models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.diagnosis

  def get_absolute_url(self):
    return reverse('postsegs_detail', kwargs={'pk': self.id})

class AntsegPhoto(models.Model):
  url = models.CharField(max_length=250)
  antseg = models.OneToOneField(Antseg, on_delete=models.CASCADE)

class PostsegPhoto(models.Model):
  url = models.CharField(max_length=250)
  postseg = models.OneToOneField(Postseg, on_delete=models.CASCADE)