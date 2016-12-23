from django.contrib import admin
from book.models import Book

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['book']
    list_display_links = ['book']
    search_fields = ['book']
    search_fields = ['book']
    list_editable = ['book']
    
    class Meta:
        model = Book


admin.site.register(Book)