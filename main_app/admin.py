from django.contrib import admin
from .models import Antseg, Postseg, PostsegPhoto, AntsegPhoto

# Register your models here.
admin.site.register(Antseg)
admin.site.register(Postseg)
admin.site.register(PostsegPhoto)
admin.site.register(AntsegPhoto)