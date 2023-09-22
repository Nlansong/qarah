from django.contrib import admin
from .models import  Tag, Category, Post

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        
    list_display = [
        'title',
        'publish_date',
        'author',
    ]
    search_fields = [
        'title',
        'body',
    ]
    prepopulated_fields = {
        'slug':('title',)
    }

admin.site.register(Post,PostAdmin)
