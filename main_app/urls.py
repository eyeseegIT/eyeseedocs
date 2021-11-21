from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path("antsegs/", views.antsegs_index, name="antsegs_index"),

  path("antsegs/<int:antseg_id>", views.antsegs_detail, name="antsegs_detail"),

  path("antsegs/create/", views.AntsegCreate.as_view(), name="antsegs_create"),

  path("antsegs/<int:pk>/update/", views.AntsegUpdate.as_view(), name="antsegs_update"),

  path("antsegs/<int:pk>/delete/", views.AntsegDelete.as_view(), name="antsegs_delete"),
]