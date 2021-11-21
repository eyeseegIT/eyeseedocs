from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path("antsegs/", views.antsegs_index, name="antsegs_index"),

  path("antsegs/<int:antseg_id>", views.antsegs_detail, name="antsegs_detail")
]