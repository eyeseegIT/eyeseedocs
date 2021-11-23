from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path("antsegs/", views.antsegs_index, name="antsegs_index"),

  path("antsegs/<int:antseg_id>/", views.antsegs_detail, name="antsegs_detail"),

  path("antsegs/create/", views.AntsegCreate.as_view(), name="antsegs_create"),

  path("antsegs/<int:pk>/update/", views.AntsegUpdate.as_view(), name="antsegs_update"),

  path("antsegs/<int:pk>/delete/", views.AntsegDelete.as_view(), name="antsegs_delete"),

  path("postsegs/create/", views.PostsegCreate.as_view(), name="postsegs_create"),

  path("postsegs/<int:pk>/", views.PostsegDetail.as_view(), name="postsegs_detail"),

  path("postsegs/", views.PostsegList.as_view(), name="postsegs_index"),

  path("postsegs/<int:pk>/update/", views.PostsegUpdate.as_view(), name="postsegs_update"),

  path("postsegs/<int:pk>/delete/", views.PostsegDelete.as_view(), name="postsegs_delete"),

  path('antsegs/<int:antseg_id>/add_antseg_photo/', views.add_antseg_photo, name='add_antseg_photo'),

  path('postsegs/<int:postseg_id>/add_postseg_photo/', views.add_postseg_photo, name='add_postseg_photo'),
]