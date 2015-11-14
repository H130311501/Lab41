from django.contrib import admin
from BookDB.models import Author,Book
class AuthorAdmin(admin.ModelAdmin):
    list_display=('AuthorID','Name','Age','Country')
    
class BookAdmin(admin.ModelAdmin):
     list_display=('ISBN','Title','AuthorID','Authorname','Publisher',
     'Publicationdate','Price')
     search_fields=('Authorname',)
     list_filter=('Publicationdate',)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
# Register your models here.
