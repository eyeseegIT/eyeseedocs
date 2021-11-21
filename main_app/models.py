from django.db import models

# Create your models here.
class Antseg(models.Model):
  photo=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
  diagnosis= models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.diagnosis