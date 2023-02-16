from django.contrib import admin
from .models import Image, ImageThumbnail

class ImageThumbnailInline(admin.TabularInline):
	model = ImageThumbnail

class ImageAdmin(admin.ModelAdmin):
	inlines = [
		ImageThumbnailInline,
	]

admin.site.register(Image,ImageAdmin)

