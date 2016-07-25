from django.contrib import admin
# from nhub.models import Users
from students.models import Music
from students.models import Contact
from students.models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display_links=('name',)
	list_display=('name','subject','message','email')
	list_per_page=10

admin.site.register(Contact,ContactAdmin)
class MusicAdmin(admin.ModelAdmin):
	list_display_links=('artiste', 'title')
	list_display=('artiste', 'title')
	list_per_page=15

admin.site.register(Music,MusicAdmin)

class ArticlesAdmin(admin.ModelAdmin):
	list_display=('article_no', 'published_date')
	

admin.site.register(Articles,ArticlesAdmin)
