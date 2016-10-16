from django.contrib import admin

# Register your models here.
from .models import Post,UserPost

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "content","updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["title", "content"]
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)


class PostUserModelAdmin(admin.ModelAdmin):
	list_display = ["title", "content", "image","updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title","image"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["title", "content"]
	class Meta:
		model = UserPost


admin.site.register(UserPost, PostUserModelAdmin)