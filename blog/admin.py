from django.contrib import admin
from blog.models import Category, Comment, Post

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)