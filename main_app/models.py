from django.db import models
from django.urls import reverse

# Create your models here.
class Antseg(models.Model):
  photo=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
  diagnosis= models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.diagnosis

  def get_absolute_url(self):
    return reverse('antsegs_detail', kwargs={'antseg_id': self.id})

class Postseg(models.Model):
  photo=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
  diagnosis= models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.diagnosis

  def get_absolute_url(self):
    return reverse('postsegs_detail', kwargs={'pk': self.id})