from . models import Post
from django.contrib import admin

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'content', 'date_posted')


admin.site.register(Post, PostAdmin)
