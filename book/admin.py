from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "rating"]
    search_fields = ["title", "owner"]
    list_filter = ["owner",]


admin.site.register(Book, BookAdmin)