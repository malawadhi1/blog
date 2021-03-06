from django.contrib import admin

from .models import Post


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp", "content", "updated"]
	list_filter = ["timestamp"]
	search_fields = ["title", "content"]
	list_display_links = ["timestamp"]
	list_editable = ["title"]


class Meta:
	model = Post

admin.site.register(Post, PostModelAdmin)
