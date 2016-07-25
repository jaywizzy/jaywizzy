from django.contrib import admin
from . models import Post
from . models import UserLogin

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ["__str__", "content","published_date", "updated", "time_stamp"]
	list_display_links = ["updated", "__str__"]
	list_filter = ["updated", "time_stamp"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post
admin.site.register(Post, PostAdmin)
admin.site.register(UserLogin)