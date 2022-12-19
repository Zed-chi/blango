from django.contrib import admin

from .models import AuthorProfile, Comment, Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(AuthorProfile)
