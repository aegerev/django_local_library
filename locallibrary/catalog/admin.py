from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')

    fields=['first_name', 'last_name', ('date_of_birth')]
admin.site.register(Author, AuthorAdmin)


admin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = ((None, {
        'fields': ('book', 'imprint', 'id')
    }),
    ('Availability', {
        'fields': ('status', 'due_back')
    }),
)

admin.site.register(Language)


